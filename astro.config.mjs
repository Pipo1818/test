// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://pflege-planet.de',
  // URLs mit abschließendem Slash – wie die Originalseite (/pflegebox/ …)
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
});
