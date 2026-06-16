import './globals.css';
import { headerHtml, footerHtml } from '@/app/content';
import Interactions from '@/components/Interactions';

export const metadata = {
  metadataBase: new URL('https://pflege-planet.de'),
  title: {
    default: 'Kostenlose Pflegehilfsmittel mit der Pflegebox von Pflegeplanet',
    template: '%s',
  },
  description:
    'Kostenlose Pflegehilfsmittel mit der Pflegebox von Pflegeplanet – im Wert von bis zu 42 € pro Monat.',
  icons: { icon: '/assets/img/logo.svg' },
};

export default function RootLayout({ children }) {
  return (
    <html lang="de">
      <body>
        <div dangerouslySetInnerHTML={{ __html: headerHtml }} />
        <main>{children}</main>
        <div dangerouslySetInnerHTML={{ __html: footerHtml }} />
        <Interactions />
      </body>
    </html>
  );
}
