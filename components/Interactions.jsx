'use client';

import { useEffect } from 'react';
import { usePathname } from 'next/navigation';

/**
 * Clientseitige Interaktionen (Port von main.js):
 * - Mobile-Navigation (Toggle)
 * - FAQ-Accordion
 * - aktive Navigationsmarkierung
 * - Kontaktformular (Submit abfangen, bis ein Backend angebunden ist)
 *
 * Da Header/Footer/Kontakt als HTML-Partials gerendert werden, verdrahten
 * wir die Interaktionen nach dem Mount per DOM. Läuft bei jedem Routenwechsel neu.
 */
export default function Interactions() {
  const pathname = usePathname();

  useEffect(() => {
    const cleanups = [];
    const on = (el, ev, fn) => {
      el.addEventListener(ev, fn);
      cleanups.push(() => el.removeEventListener(ev, fn));
    };

    // Mobile-Navigation
    const toggle = document.querySelector('.nav-toggle');
    const links = document.querySelector('.nav-links');
    if (toggle && links) {
      on(toggle, 'click', () => {
        links.classList.toggle('open');
        toggle.setAttribute(
          'aria-expanded',
          links.classList.contains('open') ? 'true' : 'false'
        );
      });
      links.querySelectorAll('a').forEach((a) =>
        on(a, 'click', () => links.classList.remove('open'))
      );
    }

    // FAQ-Accordion
    document.querySelectorAll('.faq-q').forEach((btn) => {
      on(btn, 'click', () => {
        const item = btn.closest('.faq-item');
        const isOpen = item.classList.contains('open');
        item.parentElement
          .querySelectorAll('.faq-item.open')
          .forEach((o) => o !== item && o.classList.remove('open'));
        item.classList.toggle('open', !isOpen);
        btn.setAttribute('aria-expanded', !isOpen ? 'true' : 'false');
      });
    });

    // Aktive Navigationsmarkierung
    document.querySelectorAll('.nav-links a').forEach((a) => {
      const href = a.getAttribute('href');
      a.classList.remove('active');
      if (!href || href.charAt(0) === '#') return;
      if (href === pathname || (href !== '/' && pathname.startsWith(href))) {
        a.classList.add('active');
      }
    });

    // Kontaktformular
    document.querySelectorAll('[data-contact-form]').forEach((form) => {
      const status = form.querySelector('[data-form-status]');
      on(form, 'submit', (e) => {
        e.preventDefault();
        if (!form.checkValidity()) {
          form.reportValidity();
          return;
        }
        if (status) {
          status.textContent =
            'Vielen Dank! Ihre Nachricht wurde erfasst. Wir melden uns in Kürze bei Ihnen.';
          status.classList.add('ok');
        }
        form.reset();
      });
    });

    return () => cleanups.forEach((fn) => fn());
  }, [pathname]);

  return null;
}
