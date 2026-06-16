import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Kostenlose Pflegehilfsmittel mit der Pflegebox von Pflegeplanet",
  description: "Zum Verbrauch bestimmte Pflegehilfsmittel mit der Pflegebox von Pflegeplanet im Wert von bis zu 42 € pro Monat – individuell, bedarfsgerecht und ohne Versandkosten. Wir übernehmen die Formalitäten.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.home }} />
      <Contact />
    </>
  );
}
