import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Pflegebox – kostenlose Pflegehilfsmittel beantragen | Pflegeplanet",
  description: "Die Pflegebox von Pflegeplanet: zuzahlungsfreie Pflegehilfsmittel im Wert von bis zu 42 € pro Monat, individuell zusammenstellbar und bequem nach Hause geliefert.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.pflegebox }} />
      <Contact />
    </>
  );
}
