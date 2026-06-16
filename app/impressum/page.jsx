import { bodies } from '@/app/content';

export const metadata = {
  title: "Impressum | Pflegeplanet",
  description: "Impressum der Pflegeplanet GmbH – Angaben gemäß § 5 Telemediengesetz.",
  robots: { index: false, follow: false },
};

export default function Page() {
  return (
    <>
      <div dangerouslySetInnerHTML={{ __html: bodies.impressum }} />
    </>
  );
}
