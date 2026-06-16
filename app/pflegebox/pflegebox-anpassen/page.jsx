import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Pflegebox anpassen – Inhalt individuell zusammenstellen | Pflegeplanet",
  description: "Stellen Sie Ihre Pflegebox individuell zusammen: Inhalt jederzeit anpassen, Lieferintervall ändern, aussetzen oder kündigen.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.anpassen }} />
      <Contact />
    </>
  );
}
