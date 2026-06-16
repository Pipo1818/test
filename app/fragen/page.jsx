import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Fragen & Antworten zur Pflegebox | Pflegeplanet",
  description: "Häufige Fragen und Antworten rund um die Pflegebox von Pflegeplanet: Anspruch, Pflegegrad, Bestellung, Lieferung, Anpassung und Kündigung.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.fragen }} />
      <Contact />
    </>
  );
}
