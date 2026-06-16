import { bodies } from '@/app/content';
import Contact from '@/components/Contact';

export const metadata = {
  title: "Über uns – unsere Vision & Mission | Pflegeplanet",
  description: "Die Menschen und die Vision hinter Pflegeplanet: Wir denken die Versorgung mit Pflegehilfsmitteln neu – so individuell und so einfach wie möglich für pflegende Angehörige.",
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.ueber }} />
      <Contact />
    </>
  );
}
