// news-image-20261125 — entrypoint.
// Copies the drawn front page (entry.png, shipped beside this file) to the
// grader's output directory, after checking it is a well-formed PNG inside
// the competition limits. Node 22, standard library only, no network.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576;
const MAX_SIDE = 1024;

function fail(message: string): never {
  throw new Error("news-image-20261125: " + message);
}

function checkPng(bytes: Buffer): void {
  if (bytes.length < 33) fail("entry.png is too short to be a PNG");
  if (!bytes.subarray(0, 8).equals(PNG_MAGIC)) fail("entry.png has a bad PNG signature");
  if (bytes.length > MAX_BYTES) fail(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`);
  if (bytes.toString("ascii", 12, 16) !== "IHDR") fail("entry.png has no IHDR chunk");
  const width = bytes.readUInt32BE(16);
  const height = bytes.readUInt32BE(20);
  if (width > MAX_SIDE || height > MAX_SIDE) {
    fail(`entry.png is ${width}x${height}, over the 1024x1024 cap`);
  }
  console.log(`entry.png OK: ${width}x${height}, ${bytes.length} bytes`);
}

const here = dirname(fileURLToPath(import.meta.url));
const picture = readFileSync(join(here, "entry.png"));
checkPng(picture);

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const target = join(outDir, "entry.png");
writeFileSync(target, picture);

const roundTrip = readFileSync(target);
if (!roundTrip.equals(picture)) fail("round-trip bytes differ from entry.png");
if (!roundTrip.subarray(0, 8).equals(PNG_MAGIC)) {
  fail("written entry.png lost its PNG signature");
}
console.log(`wrote ${target} (${roundTrip.length} bytes, byte-identical)`);
