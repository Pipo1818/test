import { contactHtml } from '@/app/content';

// Kontaktsektion (HTML-Partial). Interaktivität via components/Interactions.jsx
export default function Contact() {
  return <div dangerouslySetInnerHTML={{ __html: contactHtml }} />;
}
