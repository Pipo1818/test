# -*- coding: utf-8 -*-
"""Seiten-Inhalte (Body) für den Pflegeplanet-Nachbau. Von build.py aufgerufen."""

def build(page, c):
    card = c["card"]; prod = c["prod"]
    I_SHIELD=c["I_SHIELD"]; I_TRUCK=c["I_TRUCK"]; I_DOC=c["I_DOC"]; I_EDIT=c["I_EDIT"]
    I_CLOCK=c["I_CLOCK"]; I_PAUSE=c["I_PAUSE"]; I_LEAF=c["I_LEAF"]
    P_GLOVE=c["P_GLOVE"]; P_DIS=c["P_DIS"]; P_SURF=c["P_SURF"]; P_FFP2=c["P_FFP2"]
    P_MASK=c["P_MASK"]; P_BED=c["P_BED"]; P_APRON=c["P_APRON"]; P_FINGER=c["P_FINGER"]

    # ===================== PFLEGEBOX =====================
    pflegebox = f"""    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="/">Startseite</a> / Pflegebox</div>
        <h1>Die Pflegebox von <span class="soft">Pflegeplanet</span></h1>
        <p>Erhalten Sie zuzahlungsfreie Pflegehilfsmittel im Wert von bis zu 42 € pro Monat – in einem von Ihnen gewählten Lieferintervall direkt nach Hause geliefert.</p>
        <div class="hero-actions" style="margin-top:24px">
          <a href="/pflegehilfsmittel-katalog/" class="btn btn--primary btn--lg">Pflegebox beantragen</a>
          <a href="/pflegebox/pflegebox-anpassen/" class="btn btn--outline btn--lg">Box anpassen</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="split">
          <div>
            <span class="eyebrow">§ 40 SGB XI</span>
            <h2>Ihr gesetzlicher Anspruch auf bis zu 42 € im Monat</h2>
            <p>Als pflegebedürftige Person mit einem anerkannten Pflegegrad haben Sie gemäß § 40 SGB XI einen Anspruch auf zuzahlungsfreie Pflegehilfsmittel zum Verbrauch im Wert von bis zu 42 € pro Monat. Die Kosten dafür werden vollständig von Ihrer Pflegekasse übernommen.</p>
            <p>So erhalten Sie hochwertige Pflegehilfsmittel, die Sie sonst selbst kaufen müssten, komplett kostenfrei. Wir stellen Ihnen eine individuell auf Ihre Bedürfnisse abgestimmte Box zusammen und schicken Sie Ihnen direkt nach Hause.</p>
            <ul class="checklist" style="margin-top:20px">
              <li>Anerkannter Pflegegrad 1 bis 5</li>
              <li>Versorgung im häuslichen Umfeld</li>
              <li>Eingetragene Pflegeperson (z. B. Angehörige)</li>
            </ul>
          </div>
          <div class="split-media">
            <svg viewBox="0 0 400 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-label="Pflegebox">
              <rect width="400" height="320" fill="#bcd6cd"/>
              <rect x="120" y="110" width="160" height="120" rx="10" fill="#305850"/>
              <path d="M120 150h160" stroke="#aac63e" stroke-width="6"/>
              <text x="200" y="200" fill="#fff" font-family="Quicksand" font-size="22" text-anchor="middle">Pflegebox</text>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="center maxw" style="margin:0 auto 48px"><span class="eyebrow">Ihre Vorteile</span><h2>Warum die Pflegebox von Pflegeplanet?</h2></div>
        <div class="grid grid-3">
          {card(I_TRUCK,'Regelmäßig &amp; versandkostenfrei','Die Pflegebox wird regelmäßig direkt zu Ihnen nach Hause geliefert – ganz ohne Versandkosten.')}
          {card(I_EDIT,'Jederzeit anpassbar','Sie können den Inhalt Ihrer Pflegebox jederzeit anpassen, aussetzen oder kündigen.')}
          {card(I_DOC,'Keine Bürokratie','Pflegeplanet übernimmt die direkte Abrechnung mit Ihrer Pflegekasse – Sie müssen sich um nichts kümmern.')}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="center maxw" style="margin:0 auto 50px"><span class="eyebrow">So funktioniert's</span><h2>Beantragen Sie in nur 3 Schritten Ihre Pflegebox</h2></div>
        <div class="steps">
          <div class="step"><div class="ico">{I_DOC}</div><h3>1. Pflegebox individuell zusammenstellen</h3><p>Stellen Sie Ihre Pflegebox ganz nach Ihrem Bedarf zusammen.</p></div>
          <div class="step"><div class="ico">{I_EDIT}</div><h3>2. Pflegedaten eingeben und Wunschtermin festlegen</h3><p>Hinterlegen Sie die nötigen Lieferdaten, damit wir Ihre Pflegebox schnellstmöglich versenden können.</p></div>
          <div class="step"><div class="ico">{I_CLOCK}</div><h3>3. Antrag online unterschreiben – fertig!</h3><p>Ihre Pflegebox wird in wenigen Tagen zugestellt.</p></div>
        </div>
        <div class="center" style="margin-top:42px"><a href="/pflegehilfsmittel-katalog/" class="btn btn--primary btn--lg">Pflegebox beantragen</a></div>
      </div>
    </section>
"""
    page("pflegebox/index.html",
         "Pflegebox – kostenlose Pflegehilfsmittel beantragen | Pflegeplanet",
         "Die Pflegebox von Pflegeplanet: zuzahlungsfreie Pflegehilfsmittel im Wert von bis zu 42 € pro Monat, individuell zusammenstellbar und bequem nach Hause geliefert.",
         pflegebox)

    # ===================== BOX ANPASSEN =====================
    anpassen = f"""    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="/">Startseite</a> / <a href="/pflegebox/">Pflegebox</a> / Box anpassen</div>
        <h1>Ihre Pflegebox individuell <span class="soft">anpassen</span></h1>
        <p>Jeder Pflegealltag ist anders. Deshalb stellen Sie Ihre Pflegebox genau so zusammen, wie Sie sie brauchen – und passen Inhalt, Menge und Lieferintervall jederzeit flexibel an.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="grid grid-3">
          {card(I_EDIT,'Inhalt anpassen','Wählen Sie genau die Pflegehilfsmittel aus, die Sie wirklich benötigen – und ändern Sie die Zusammenstellung jederzeit.')}
          {card(I_CLOCK,'Lieferintervall wählen','Bestimmen Sie selbst, in welchem Intervall Ihre Pflegebox geliefert wird – passend zu Ihrem Verbrauch.')}
          {card(I_PAUSE,'Aussetzen &amp; kündigen','Sie können die Lieferung jederzeit pausieren oder kündigen – ohne lange Fristen oder versteckte Kosten.')}
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split">
          <div>
            <span class="eyebrow">Maximale Flexibilität</span>
            <h2>Immer genau das, was Sie brauchen</h2>
            <p>Sie können den Inhalt Ihrer Pflegebox jederzeit anpassen, aussetzen oder kündigen. Ob mehr Einmalhandschuhe, zusätzliche Flächendesinfektion oder andere Bettschutzeinlagen – Ihre Box passt sich Ihrem Alltag an, nicht umgekehrt.</p>
            <p>Eine kurze Nachricht über unser Kontaktformular oder ein Anruf genügt. Unser Team setzt Ihre Wünsche zum gewünschten Zeitpunkt um.</p>
            <a href="/pflegehilfsmittel-katalog/" class="btn btn--primary btn--lg" style="margin-top:8px">Zum Produktkatalog</a>
          </div>
          <div class="split-media"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg></div>
        </div>
      </div>
    </section>
"""
    page("pflegebox/pflegebox-anpassen/index.html",
         "Pflegebox anpassen – Inhalt individuell zusammenstellen | Pflegeplanet",
         "Stellen Sie Ihre Pflegebox individuell zusammen: Inhalt jederzeit anpassen, Lieferintervall ändern, aussetzen oder kündigen.",
         anpassen)

    # ===================== KATALOG =====================
    katalog = f"""    <section class="page-hero">
      <div class="container">
        <div class="crumbs"><a href="/">Startseite</a> / Pflegehilfsmittel-Katalog</div>
        <h1>Pflegehilfsmittel-Katalog</h1>
        <p>Wir haben es uns zur Aufgabe gemacht, die Versorgung Pflegebedürftiger mit Pflegehilfsmitteln zu revolutionieren. Mit hochwertigen Produkten namhafter Hersteller sorgen wir für maximale Kundenzufriedenheit.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="products">
          {prod(P_DIS,'Handdesinfektion')}
          {prod(P_SURF,'Flächendesinfektion')}
          {prod(P_GLOVE,'Einmalhandschuhe')}
          {prod(P_FFP2,'FFP2 Mundschutz')}
          {prod(P_MASK,'Medizinischer Mundschutz')}
          {prod(P_BED,'Bettschutzeinlagen Mehrfachgebrauch')}
          {prod(P_BED,'Bettschutzeinlagen Einmalgebrauch')}
          {prod(P_APRON,'Schutzschürzen')}
        </div>
        <div class="center" style="margin-top:46px">
          <p class="lead" style="margin:0 auto 24px">Laut § 40 SGB XI besteht bei vorliegendem Pflegegrad ein Anspruch auf Pflegehilfsmittel zum Verbrauch im Wert von bis zu 42 € pro Monat – wir stellen Ihre Box individuell zusammen.</p>
          <a href="/pflegebox/" class="btn btn--primary btn--lg">Box zusammenstellen &amp; beantragen</a>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="center maxw" style="margin:0 auto 48px"><span class="eyebrow">Geprüfte Qualität</span><h2>Hochwertige Produkte namhafter Hersteller</h2></div>
        <div class="grid grid-3">
          {card(I_SHIELD,'Markenqualität','Wir setzen ausschließlich auf hochwertige Pflegehilfsmittel ausgewählter Lieferanten – z. B. Hände- und Flächendesinfektion von MaiMed.')}
          {card(I_LEAF,'Hautverträglich','Produkte für die tägliche Anwendung – schonend zur Haut und zuverlässig im Schutz.')}
          {card(I_TRUCK,'Bequem geliefert','Alle Produkte kommen versandkostenfrei in Ihrer individuellen Pflegebox nach Hause.')}
        </div>
      </div>
    </section>
"""
    page("pflegehilfsmittel-katalog/index.html",
         "Pflegehilfsmittel-Katalog – alle Produkte im Überblick | Pflegeplanet",
         "Der Pflegehilfsmittel-Katalog von Pflegeplanet: Handdesinfektion, Flächendesinfektion, Einmalhandschuhe, FFP2- und medizinischer Mundschutz, Bettschutzeinlagen und Schutzschürzen.",
         katalog)

    # ===================== FRAGEN =====================
    def faq(q, a, open_=False):
        cls = " open" if open_ else ""
        exp = "true" if open_ else "false"
        return f'<div class="faq-item{cls}"><button class="faq-q" aria-expanded="{exp}">{q}</button><div class="faq-a"><div>{a}</div></div></div>'

    fragen = f"""    <section class="hero-dark">
      <div class="container">
        <span class="eyebrow">Wir lassen keine Frage unbeantwortet!</span>
        <h1>Fragen &amp; Antworten</h1>
        <p>Hier finden Sie strukturiert alle Informationen zur Pflegebox von Pflegeplanet.</p>
        <p>Häufig gestellte Fragen werden kurzfristig auf der Webseite eingebunden und von unserem Team beantwortet. Sollte Ihre Frage noch nicht aufgeführt sein, schreiben Sie uns gerne über unser Kontaktformular:</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="faq">
          {faq('Wer hat monatlichen Anspruch auf eine Pflegebox?',
               'Anspruch auf eine Pflegebox haben:<ol><li>Pflegebedürftige mit einem anerkannten Pflegegrad 1-5.</li><li>Pflegebedürftige, die in der Häuslichkeit wohnen.</li><li>Pflegebedürftige, die über eine eingetragene Pflegeperson verfügen. Meist sind es die Kinder oder nahe Angehörige.</li></ol>', open_=True)}
          {faq('Wie kann ich die Pflegebox bestellen?',
               'Sie können den Antrag bequem online ausfüllen und direkt absenden. Alternativ rufen Sie uns unter 0800 988 60 53 an – wir helfen Ihnen beim Ausfüllen der Formulare und senden Ihnen diese zur Unterschrift zu.')}
          {faq('Wie lange dauert es, bis ich meine erste Pflegebox nach Hause geliefert bekomme?',
               'Nach Eingang Ihres unterschriebenen Antrags wird Ihre Pflegebox in der Regel innerhalb weniger Tage zusammengestellt und versandt.')}
          {faq('Kann ich die Produkte in der Pflegebox nachträglich ändern?',
               'Ja. Sie können den Inhalt Ihrer Pflegebox jederzeit anpassen, aussetzen oder kündigen – ganz nach Ihrem Bedarf. Mehr dazu unter <a href="/pflegebox/pflegebox-anpassen/">Pflegebox anpassen</a>.')}
          {faq('Wie kann ich die Pflegebox kündigen?',
               'Die Pflegebox können Sie jederzeit kündigen. Senden Sie uns einfach eine Nachricht über unser Kontaktformular, und wir stoppen Ihre Versorgung zum gewünschten Zeitpunkt.')}
        </div>
      </div>
    </section>
"""
    page("fragen/index.html",
         "Fragen & Antworten zur Pflegebox | Pflegeplanet",
         "Häufige Fragen und Antworten rund um die Pflegebox von Pflegeplanet: Anspruch, Pflegegrad, Bestellung, Lieferung, Anpassung und Kündigung.",
         fragen)

    # ===================== ÜBER UNS =====================
    ueber = f"""    <section class="page-hero">
      <div class="container">
        <div class="split-media" style="aspect-ratio:21/6;margin-bottom:36px">
          <svg viewBox="0 0 1200 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" aria-label="Das Team von Pflegeplanet">
            <rect width="1200" height="320" fill="#bcd6cd"/>
            <circle cx="380" cy="150" r="60" fill="#efe0d4"/><circle cx="560" cy="140" r="66" fill="#e7d3c4"/><circle cx="740" cy="150" r="58" fill="#f0e2d6"/>
            <path d="M280 320c0-66 46-114 100-114s100 44 100 100" fill="#9cbfb5"/>
            <path d="M470 320c4-66 50-112 110-112s108 44 112 112z" fill="#88b1a6"/>
            <path d="M660 320c2-62 46-108 104-108s104 44 108 108z" fill="#9cbfb5"/>
          </svg>
        </div>
        <h1>Die Menschen hinter <span class="soft">Pflegeplanet</span></h1>
      </div>
    </section>

    <section class="section">
      <div class="container" style="max-width:880px">
        <span class="eyebrow">Das sind wir</span>
        <h2>Die Menschen und die Vision hinter Pflegeplanet</h2>
        <p>Pflege ist Vertrauens- und Herzenssache. Nahezu jede Familie kommt irgendwann mit dem Thema Pflege in Berührung – oft plötzlich und unerwartet. Ab diesem Moment merken alle Beteiligten, wie komplex und zum Teil nervenaufreibend die Organisation – auch von Pflegehilfsmitteln – sein kann. Genau an diesem Punkt setzt Pflegeplanet an.</p>
        <p>Wir verfolgen die <strong>Vision</strong>, die Versorgung mit Pflegehilfsmitteln so <strong>individuell</strong> wie möglich und die Organisation für die pflegenden Angehörigen so <strong>einfach</strong> wie möglich zu gestalten. Dafür nutzen wir alle zur Verfügung stehenden technischen Möglichkeiten und digitalisieren die oft bürokratischen Prozesse, mit denen sich Pflegebedürftige und ihre Angehörigen auseinandersetzen müssen.</p>
      </div>
    </section>

    <section class="section section--alt">
      <div class="container">
        <div class="split reverse">
          <div>
            <span class="eyebrow">Unsere Mission</span>
            <h2>Versorgung neu gedacht</h2>
            <p>Pflegeplanet hat es sich zur Aufgabe gemacht, die Versorgung mit Pflegehilfsmitteln neu zu denken. Wir haben uns auf die Bedürfnisse von Pflegebedürftigen und ambulanten Pflegeeinrichtungen spezialisiert und Angebote entwickelt, die wir kontinuierlich erweitern.</p>
            <p>Dabei setzen wir ausschließlich auf hochwertige Pflegehilfsmittel und ausgewählte Lieferanten – für höchste Qualität und maximale Kundenzufriedenheit.</p>
          </div>
          <div class="split-media"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.1"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="center maxw" style="margin:0 auto 48px"><span class="eyebrow">So unterstützen wir Sie</span><h2>Erfahrung, die man spürt</h2><p class="lead" style="margin-left:auto;margin-right:auto">Durch langjährige Erfahrung in der Pflege stehen wir Ihnen kompetent zur Seite. Durch unser stetig wachsendes Angebot optimieren wir unsere Leistungen kontinuierlich.</p></div>
        <div class="grid grid-3">
          {card(I_DOC,'Kompetente Beratung','Langjährige Erfahrung in der Pflege – persönlich und auf Augenhöhe.')}
          {card(I_LEAF,'Stetiges Wachstum','Wir erweitern unser Angebot kontinuierlich und optimieren unsere Leistungen.')}
          {card(I_SHIELD,'Geprüfte Qualität','Ausschließlich hochwertige Hilfsmittel namhafter Hersteller und ausgewählter Lieferanten.')}
        </div>
      </div>
    </section>
"""
    page("ueber-uns/index.html",
         "Über uns – unsere Vision & Mission | Pflegeplanet",
         "Die Menschen und die Vision hinter Pflegeplanet: Wir denken die Versorgung mit Pflegehilfsmitteln neu – so individuell und so einfach wie möglich für pflegende Angehörige.",
         ueber)

    # ===================== IMPRESSUM =====================
    impressum = """    <section class="page-hero">
      <div class="container"><div class="crumbs"><a href="/">Startseite</a> / Impressum</div><h1>Impressum</h1></div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>Inhaltlich Verantwortlicher gemäß § 5 Telemediengesetz ist:</h2>
        <address>
          <strong>Pflegeplanet GmbH</strong><br />
          Spreebordstr. 20<br />
          15537 Gosen-Neu Zittau
        </address>
        <p>
          Tel.: <a href="tel:08009886053" class="lime">0800 988 60 53</a><br />
          E-Mail: <a href="mailto:info@pflege-planet.de">info@pflege-planet.de</a>
        </p>
        <p>
          Geschäftsführer: Tim Bodung<br />
          Handelsregister: HRB 18917 Amtsgericht Frankfurt (Oder)<br />
          Ust.-IdNr.: <span class="lime">DE 347 859 978</span><br />
          IK: 331206362
        </p>
        <p>Inhaltlich Verantwortlicher gemäß § 55 Abs. 2 RStV: Tim Bodung</p>

        <h2>Haftungsbeschränkung</h2>
        <p>Die Inhalte dieser Website werden von der Pflegeplanet GmbH mit größtmöglicher Sorgfalt erstellt. Die Pflegeplanet GmbH übernimmt jedoch keine Gewähr für die Richtigkeit, Vollständigkeit und Aktualität der bereitgestellten Inhalte. Aus diesem Grund ist jegliche Haftung für eventuelle Schäden im Zusammenhang mit der Nutzung des Informationsangebots ausgeschlossen.</p>

        <h2>Hinweis zu externen Links</h2>
        <p>Diese Website enthält Verknüpfungen zu Websites von anderen Anbietern. Die Pflegeplanet GmbH hat bei der erstmaligen Verknüpfung der externen Links die fremden Inhalte daraufhin überprüft, ob etwaige Rechtsverstöße bestehen. Zu diesem Zeitpunkt waren keine Rechtsverstöße ersichtlich. Die Pflegeplanet GmbH hat keinen Einfluss auf die aktuelle und zukünftige Gestaltung und auf die Inhalte der verknüpften Seiten. Die Links werden regelmäßig auf vorliegende Rechtsverstöße überprüft und bei einer Rechtsverletzung unverzüglich entfernt. Die Bereitstellung der externen Links bedeutet nicht, dass sich Pflegeplanet GmbH den Inhalt der hinter dem Verweis liegenden Seiten zu eigen macht.</p>

        <h2>Urheberrechte</h2>
        <p>Die auf dieser Website veröffentlichten Inhalte und Werke unterliegen dem deutschen Urheberrecht. Jede Art der Vervielfältigung, Bearbeitung, Verbreitung und Verwertung außerhalb der Grenzen des Urheberrechts bedarf der vorherigen schriftlichen Zustimmung der Pflegeplanet GmbH bzw. des jeweiligen Urhebers.</p>
      </div>
    </section>
"""
    page("impressum/index.html", "Impressum | Pflegeplanet",
         "Impressum der Pflegeplanet GmbH – Angaben gemäß § 5 Telemediengesetz.",
         impressum, noindex=True, contact=False)

    # ===================== DATENSCHUTZ =====================
    datenschutz = """    <section class="page-hero">
      <div class="container"><div class="crumbs"><a href="/">Startseite</a> / Datenschutz</div><h1>Datenschutzerklärung</h1></div>
    </section>
    <section class="section">
      <div class="container prose">
        <h2>1. Datenschutz auf einen Blick</h2>
        <h3>Allgemeine Hinweise</h3>
        <p>Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können. Ausführliche Informationen zum Thema Datenschutz entnehmen Sie unserer unter diesem Text aufgeführten Datenschutzerklärung.</p>
        <h3>Datenerfassung auf dieser Website</h3>
        <p><strong>Wer ist verantwortlich für die Datenerfassung auf dieser Website?</strong><br />Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber. Dessen Kontaktdaten können Sie dem Abschnitt „Hinweis zur verantwortlichen Stelle" in dieser Datenschutzerklärung entnehmen.</p>
        <p><strong>Wie erfassen wir Ihre Daten?</strong><br />Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen. Hierbei kann es sich z. B. um Daten handeln, die Sie in ein Kontaktformular eingeben. Andere Daten werden automatisch oder nach Ihrer Einwilligung beim Besuch der Website durch unsere IT-Systeme erfasst. Das sind vor allem technische Daten (z. B. Internetbrowser, Betriebssystem oder Uhrzeit des Seitenaufrufs).</p>
        <p><strong>Wofür nutzen wir Ihre Daten?</strong><br />Ein Teil der Daten wird erhoben, um eine fehlerfreie Bereitstellung der Website zu gewährleisten. Andere Daten können zur Analyse Ihres Nutzerverhaltens verwendet werden.</p>
        <p><strong>Welche Rechte haben Sie bezüglich Ihrer Daten?</strong><br />Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen. Wenn Sie eine Einwilligung zur Datenverarbeitung erteilt haben, können Sie diese Einwilligung jederzeit für die Zukunft widerrufen. Außerdem haben Sie das Recht, unter bestimmten Umständen die Einschränkung der Verarbeitung Ihrer personenbezogenen Daten zu verlangen. Des Weiteren steht Ihnen ein Beschwerderecht bei der zuständigen Aufsichtsbehörde zu.</p>

        <h2>2. Hosting</h2>
        <p>Wir hosten die Inhalte unserer Website bei einem externen Dienstleister (Hoster). Die personenbezogenen Daten, die auf dieser Website erfasst werden, werden auf den Servern des Hosters gespeichert. Hierbei kann es sich v. a. um IP-Adressen, Kontaktanfragen, Meta- und Kommunikationsdaten, Vertragsdaten, Kontaktdaten, Namen, Websitezugriffe und sonstige Daten, die über eine Website generiert werden, handeln. Der Einsatz des Hosters erfolgt zum Zwecke der Vertragserfüllung gegenüber unseren potenziellen und bestehenden Kunden (Art. 6 Abs. 1 lit. b DSGVO) und im Interesse einer sicheren, schnellen und effizienten Bereitstellung unseres Online-Angebots durch einen professionellen Anbieter (Art. 6 Abs. 1 lit. f DSGVO).</p>

        <h2>3. Allgemeine Hinweise und Pflichtinformationen</h2>
        <h3>Datenschutz</h3>
        <p>Die Betreiber dieser Seiten nehmen den Schutz Ihrer persönlichen Daten sehr ernst. Wir behandeln Ihre personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung.</p>
        <h3>Hinweis zur verantwortlichen Stelle</h3>
        <p>Die verantwortliche Stelle für die Datenverarbeitung auf dieser Website ist:</p>
        <address><strong>Pflegeplanet GmbH</strong><br />Spreebordstr. 20<br />15537 Gosen-Neu Zittau<br />Telefon: <a href="tel:08009886053">0800 988 60 53</a><br />E-Mail: <a href="mailto:info@pflege-planet.de">info@pflege-planet.de</a></address>
        <p>Verantwortliche Stelle ist die natürliche oder juristische Person, die allein oder gemeinsam mit anderen über die Zwecke und Mittel der Verarbeitung von personenbezogenen Daten entscheidet.</p>
        <h3>Speicherdauer</h3>
        <p>Soweit innerhalb dieser Datenschutzerklärung keine speziellere Speicherdauer genannt wurde, verbleiben Ihre personenbezogenen Daten bei uns, bis der Zweck für die Datenverarbeitung entfällt. Wenn Sie ein berechtigtes Löschersuchen geltend machen oder eine Einwilligung zur Datenverarbeitung widerrufen, werden Ihre Daten gelöscht, sofern wir keine anderen rechtlich zulässigen Gründe für die Speicherung Ihrer personenbezogenen Daten haben.</p>
        <h3>Widerruf Ihrer Einwilligung zur Datenverarbeitung</h3>
        <p>Viele Datenverarbeitungsvorgänge sind nur mit Ihrer ausdrücklichen Einwilligung möglich. Sie können eine bereits erteilte Einwilligung jederzeit widerrufen. Die Rechtmäßigkeit der bis zum Widerruf erfolgten Datenverarbeitung bleibt vom Widerruf unberührt.</p>

        <h2>4. Datenerfassung auf dieser Website</h2>
        <h3>Kontaktformular</h3>
        <p>Wenn Sie uns per Kontaktformular Anfragen zukommen lassen, werden Ihre Angaben aus dem Anfrageformular inklusive der von Ihnen dort angegebenen Kontaktdaten zwecks Bearbeitung der Anfrage und für den Fall von Anschlussfragen bei uns gespeichert. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter. Die Verarbeitung dieser Daten erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Erfüllung eines Vertrags zusammenhängt oder zur Durchführung vorvertraglicher Maßnahmen erforderlich ist.</p>
        <h3>Anfrage per E-Mail oder Telefon</h3>
        <p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, wird Ihre Anfrage inklusive aller daraus hervorgehenden personenbezogenen Daten (Name, Anfrage) zum Zwecke der Bearbeitung Ihres Anliegens bei uns gespeichert und verarbeitet.</p>

        <p style="margin-top:2em;color:var(--ink-soft)"><em>Hinweis: Dies ist eine inhaltlich an das Original angelehnte Datenschutzerklärung im Rahmen des Nachbaus. Für den Live-Betrieb sollte sie rechtlich geprüft und an die tatsächlich eingesetzten Dienste angepasst werden.</em></p>
      </div>
    </section>
"""
    page("datenschutz/index.html", "Datenschutzerklärung | Pflegeplanet",
         "Datenschutzerklärung der Pflegeplanet GmbH gemäß DSGVO.",
         datenschutz, noindex=True, contact=False)
