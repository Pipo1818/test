import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Pflegehilfsmittel-Katalog – alle Produkte im Überblick | Pflegeplanet",
  description: "Der Pflegehilfsmittel-Katalog von Pflegeplanet: Handdesinfektion, Flächendesinfektion, Einmalhandschuhe, FFP2- und medizinischer Mundschutz, Bettschutzeinlagen und Schutzschürzen.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.katalog }} />
      <Contact />
    </>
  );
}
