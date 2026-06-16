import { bodies } from '@/app/content';

export const metadata = {
  title: "Datenschutzerklärung | Pflegeplanet",
  description: "Datenschutzerklärung der Pflegeplanet GmbH gemäß DSGVO.",
  robots: { index: false, follow: false },
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.datenschutz }} />
    </>
  );
}
