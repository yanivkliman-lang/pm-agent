# Yotpo Reviews, Day Zero: The Social Proof Engine
**Product Proposal | מצגת ל-50 דקות | 14 סליידים**
*יניב קלימן · מאי 2026*

---

## סליד 1: Title

# Day Zero
## The Social Proof Engine
### Solving the Cold-Start Problem for New Product Launches

*Yotpo PM Home Assignment*
*יניב קלימן · מאי 2026*

---

## סליד 2: הבעיה

### בעיית ה-"Cold Start" באיקומרס

48 השעות הראשונות אחרי השקה מכתיבות את המומנטום ארוך-הטווח של מוצר חדש. אבל מוצרים חדשים משיקים כמעט תמיד עם **אפס ביקורות**: והדאטה ברורה:

> **המחיר של אפס ביקורות**
>
> • **44%** מהצרכנים לא ירכשו מוצר ללא ביקורות *(PowerReviews, 2021)*
> • מוצרים עם **5 ביקורות בלבד** ממירים **פי 3.7** ביחס למוצרים ללא ביקורות *(Spiegel Research, Northwestern)*
> • למוצרים יקרים מעל $500: **פי 4.8** *(Spiegel Research)*
> • קנסות FTC על ביקורות מתוגמלות: עד **$51,744 להפרה**: סיכון שגובר ככל שיותר מרצ'נטים נואשים פונים לרכישת ביקורות מזויפות כדי לעקוף את ה-Cold Start

> **איך לקרוא את המספרים:**
> אם מוצר ללא ביקורות ממיר 1% מהמבקרים: אותו מוצר עם 5 ביקורות ימיר ~3.7% מהמבקרים. זה לא שיפור שולי: זה הבדל מבני בקצב ההמרה.

> **למה זה חשוב עכשיו:** השילוב בין CAC גבוה, פער ה-Cold Start, והאכיפה הגוברת של FTC יוצר ואקום בשוק. מרצ'נטים צריכים פתרון **חוקי, מובנה ואוטומטי**: בדיוק מה ש-Ignite מספק.

**הפער של Yotpo כיום:** הפלטפורמה הקיימת היא ריאקטיבית. היא מסתמכת על מכירות אורגניות ועל מחזורי שימוש לאחר רכישה לפני שמתחילות להצטבר ביקורות, זמן שהשקת מוצר חדש לא יכולה להרשות לעצמה. **חסר מנגנון פרואקטיבי שיוצר Day Zero proof.**

---

## סליד 3: קהל היעד

### שתי פרסונות מרכזיות

**המרצ'נט (Mid-Market & Enterprise D2C):**
- מותגי Fashion, Beauty, CPG עם השקות תכופות
- **כאב:** תקציבי שיווק שמתבזבזים על תעבורת Day-1, פעילות VIP ידנית בלתי-סקלבילית
- **רצון:** אוטומציה native שיוצרת Social Proof לפני ה-launch

**הסוקר (Top Loyalty Members):**
- לקוחות בטיירים העליונים של תוכנית הנאמנות
- **מוטיבציה:** Insider Status: גישה מוקדמת למוצרים סודיים, יחס מועדף מהמותג
- **תגמול:** מוצר חינם + VIP Points / Discount Code

---

## סליד 4: נוף תחרותי

### פתרונות קיימים ומגבלותיהם

| פתרון | מגבלה |
|--------|--------|
| **רשתות צד-ג'** (Influenster, BzzAgent) | "Mercenary Network": סוקרים גנריים ללא זיקה למותג |
| **פנייה ידנית ל-VIPs** | Spreadsheets, לא סקלבילי, נטוש דאטה |
| **Amazon Vine** | עובד רק בתוך הגן החומות של Amazon |

### היתרון של Yotpo: Zero-Party Data Optimization

במקום מאגר סוקרים חיצוני: שימוש בדאטה של המרצ'נט עצמו (לקוחות נאמנים + סוקרים מוכחים).
**Closed-loop, native, FTC-compliant.**

---

## סליד 5: הפתרון: Yotpo Ignite

### מנוע ההזרעה AI-Native

**Yotpo Ignite** הוא module חדש בתוך Yotpo Reviews, המופעל על ידי **Ignite Agent**: סוכן AI שמחבר שלושה נכסי דאטה קיימים:

> **אין התקנה נפרדת.** לקוחות Yotpo Reviews הקיימים מפעילים את Ignite בכפתור אחד. אין Shopify App חדש, אין onboarding חדש, אין אינטגרציה חדשה. נבנה על גבי החיבור Yotpo<>Shopify שכבר קיים.

```
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│  Yotpo Reviews   │    │   Yotpo Loyalty  │    │ Shopify Catalog  │
│   Historical     │    │    Tiers + LTV   │    │  Product Meta    │
└────────┬─────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                       │                        │
         └───────────┬───────────┴────────────────────────┘
                     ▼
              ┌──────────────┐
              │ IGNITE AGENT  │  ← AI Orchestrator
              └──────────────┘
```

**שני טיירים:**

*שני הטיירים כוללים Free Product (הבסיס התפעולי). הבחירה האסטרטגית:*

| | **Ignite Basic** | **Ignite Pro** |
|---|---|---|
| **מתאים למרצ'נטים עם** | Yotpo Reviews בלבד | Yotpo Reviews + Loyalty |
| **תגמול לאחר ביקורת** | Discount Code | VIP Loyalty Points + Insider Status |
| **התאמה אופטימלית** | השקות תכופות נמוכות, קטגוריות one-time | דרופים תכופים, מותגי LTV-focused |
| **ערך אסטרטגי** | Entry point | בונה flywheel של engagement חוזר |

> *Ignite Pro דוחף Cross-Sell טבעי ל-Yotpo Loyalty*

---

## סליד 6: Merchant Flow + Timeline + Mockup

### זרימת המרצ'נט (T-Minus 14 ימים מינימום)

> **גמישות לוח זמנים:** 14 ימים הוא ה-**מינימום** וגם ה-**default** המומלץ. המרצ'נט יכול להאריך עד 30+ ימים אם הוא מתכנן השקה גדולה.
> *תזמון קצר יותר ייבחן ב-Phase 2 בהתאם לפידבק מהלקוחות ולשיתוף פעולה עם חברות שילוח, מכיוון שמוצרים פיזיים יכולים לקחת מ-2 ימים עד שבוע להגיע: תלוי ביעד.*


```
T-14 ──→ T-13 ──→ T-13 ──→ T-12 ──→ T-10..T-2 ──→ T-24h ──→ T-0
Setup   AI Match  Approval  Opt-In   Submission   Lock    LAUNCH
                  + Ship    +Webhook   Window    Window
```

**7 שלבים אוטומטיים (timeline ניתן להארכה לפי בחירת המרצ'נט):**
1. **Setup:** המרצ'נט מחבר Product Draft, ה-AI מציע פול אופטימלי ו-incentive אופטימלי
2. **AI Match:** סורק את המוצר ומדרג סוקרים לפי Category Affinity, Review Richness, Loyalty Tier
3. **Approval:** המרצ'נט רואה רשימה עם **הסבר AI לכל סוקר** ("Sarah נבחרה כי כתבה ביקורות על 4 נעלי שטח...")
4. **Opt-In:** SMS/Email/WhatsApp לסוקר. **רק מי שמאשר → מקבל מוצר**
5. **Fulfillment + Carrier Webhook:** Shippo/AfterShip מזהה Delivery → לינק נשלח אוטומטית
6. **Submission:** Smart Review Form
7. **Lock + Launch:** 24 שעות לפני, AI נועל את הקמפיין

> **[Mockup Screen 1: Merchant Campaign Setup]**

---

## סליד 7: חוויית הסוקר + Mockup

### Smart Review Form: AI-Driven

**Dynamic Attribute Prompts**: Ignite Agent יוצר שאלות ספציפיות למוצר:
> *"איך התאימה מידת הנעל ביחס למידה הרגילה שלך?"*
> *"איך הרגיש האטימות למים בריצה בגשם?"*

**אכיפה ויזואלית:** חובה להעלות תמונה. AI סורק לאומת stock images / screenshots.

**Sentiment Authenticity Check:** ה-AI מזהה ביקורות גנריות ("great product!") ומבקש מהסוקר לפרט.

**Real-Time Quality Meter:** סרגל חי שמראה את ציון האיכות (150+ תווים = ירוק).

**FTC Disclosure:** Built-in: תיוג אוטומטי "Received free product as part of brand seeding program."

**מערכת ה-3-Strikes (Platform-Level, בלתי-נראית לסוקר):** סוקר שאישר השתתפות אך לא הגיש ביקורת איכותית תוך 5 ימים מקבל ענישה הדרגתית פנימית: **Strike 1** → דה-פריוריטיזציה בקמפיינים עתידיים · **Strike 2** → ירידה ל-tier סוקר נמוך יותר · **Strike 3** → הוצאה מרשת ה-VIP Seeding.

> **בחירת עיצוב קריטית:** Strikes הם מנגנון ציון פנימי בלבד: **לעולם לא נחשפים לסוקר.** לקוח VIP לעולם לא מקבל הודעת "קיבלת Strike". הוא פשוט מקבל פחות הזמנות עם הזמן. זה שומר על מערכת היחסים מותג-לקוח תוך שמירה על משמעת תפעולית.

**Report Issue:** כפתור ייעודי לסוקרים שקיבלו מוצר פגום: מקפיא Strike, מתריע ל-CS. מגן על VIPs לגיטימיים מענישה על בעיות שילוח/איכות שאינן בשליטתם.

> **[Mockup Screen 2: Smart Review Form]**

---

## סליד 8: Launch Dashboard + Integrity Guardrail

### חלון 24 השעות לפני Launch

המרצ'נט רואה:
- **Campaign Health Score** מצרפי (איכות, פיזור דירוגים, אותנטיות תמונות)
- כל הביקורות בתוצר Read-Only Preview
- מצב משלוחים בזמן אמת

### Integrity Guardrail

> **המרצ'נט יכול לקרוא את כל הביקורות: אבל לא יכול למחוק ביקורות בודדות לפי דירוג או sentiment.**
> שתי אפשרויות בינאריות:
> 1. **Confirm Launch**: כל הביקורות עולות ב-T-0
> 2. **Cancel Campaign**: ביטול מתועד ב-audit log לציות FTC

### Yotpo Automated Moderation (חריג ברמת הפלטפורמה)

הפרות סטנדרטיות של חוקי קהילה **כן** מסוננות: אבל לעולם לא על-פי שיקול דעת המרצ'נט. מערכת ה-Moderation האוטומטית של Yotpo מסמנת ומסירה:
- **שפה פוגענית או מסיתה**
- **תלונות לוגיסטיות מסוות כביקורת מוצר** ("החולצה הגיעה עם חור" → בעיית שילוח, לא איכות מוצר)
- **חשיפת מידע סודי** (פרטים אישיים, מחירים פנימיים, קודים)
- **טענות שגויות עובדתית על המוצר**

> המרצ'נט יכול *לבקש* moderation דרך הערוץ הזה: אבל ההחלטה מתקבלת על ידי מערכת ה-Yotpo האוטומטית לפי חוקים סטנדרטיים, **לא לפי העדפת המרצ'נט.** זה שומר על אותנטיות תוך טיפול בבעיות תוכן לגיטימיות.

### Anti-Gaming Safeguards
- **Per-Product Cooldown:** 30 יום אחרי ביטול
- **Annual Rate Limit:** עד 3 ביטולים ב-12 חודשים
- **AI Pattern Detection:** ה-Ignite Agent מזהה דפוסים חשודים (ביטולים כשהדירוג יורד מ-4.5★)

> **[Mockup Screen 3: Launch Dashboard]**

---

## סליד 9: Quality Control + Cold-Cold Start

### בקרת איכות (סיכום)

| מנגנון | תכלית |
|--------|--------|
| Dynamic Prompts (AI) | מבטל ביקורות גנריות |
| Visual Enforcement | מבטל ביקורות מזויפות |
| 150-Char Minimum | מבטל "great!" |
| Sentiment Authenticity | זיהוי copy-paste / generic praise |
| Image AI Scan | מזהה stock photos & screenshots |

### Cold-Cold Start: קטגוריה חדשה לחנות

**תרחיש:** מותג Fashion משיק לראשונה קו skincare. אין דאטה היסטורי בקטגוריה.

**הפתרון: Micro-Survey Switch:**
- AI שולח **SMS שאלה אחת לטופ 5%** של חברי loyalty (min 50, max 500)
- *"היי שרה, אנחנו משיקים משהו חדש וסודי. את משתמשת ב-SPF יומי? השב 'כן' לגישה מוקדמת חינם."*
- מי שמשיב "כן": מצטרף לפול הקמפיין

> *ה-AI מתאים את הגישה לגודל המרצ'נט: מתחת ל-50 חברי loyalty → הרחבה לבסיס Reviews הקיים*

### הגנת פול הסוקרים (Fatigue + LTV Safeguards)

מכיוון ש-Ignite משתמש בלקוחות VIP של המרצ'נט עצמו: לא ברשת חיצונית: שני סיכונים שונים נדרשים לניהול:

**סיכון Fatigue (פנייה תכופה מדי):**
- **Cooldown סטטי:** סוקר לא יכול להשתתף ביותר מ-2 קמפיינים בחלון של 90 יום
- **ניטור AI דינמי:** ה-Ignite Agent מזהה אותות עייפות אישיים (תגובת SMS איטית יותר, ביקורת קצרה יותר, איכות תמונה ירודה) ומשבית סוקרים מותשים אישית: גם לפני שהגיעו לגבול הסטטי

**סיכון LTV Cannibalization (המתנה ל-Free Drops):**
- **Holdout Group אלגוריתמי:** ה-Ignite Agent מנהל קבוצת ביקורת מובנית שמונעת קבלת מוצרים חינם ברצף לאותו לקוח VIP
- *Rationale:* אם לקוח טופ לומד שהוא מקבל באופן קבוע מוצרים חינם דרך Ignite, התנהגות הרכישה האורגנית שלו עלולה להשתנות: הוא יעכב רכישות רגילות בציפייה ל"דרופ" הבא. ה-Holdout מבטיח ש-Ignite מזריע את המשפך מבלי לשחוק את ה-LTV האורגני של הלקוחות הטובים ביותר.

---

## סליד 10: KPIs + Risks

### KPIs

**Primary Metric:**
**Product Launch CVR Lift**: אחוז שיפור ביחס המרה ב-48 השעות הראשונות, מול benchmark היסטורי של מוצרים שהושקו עם 0 ביקורות.

**Secondary Metrics:**
- **Campaign Fulfillment Rate**: % קמפיינים שהשיגו 20-30 ביקורות מאושרות בחלון ה-24
- **Review Richness Score**: ממוצע אורך + % כולל תמונות/וידאו
- **Cross-Product Adoption**: % לקוחות Reviews שהפעילו Loyalty כתוצאה מ-Ignite *(ה-business KPI של Yotpo)*

**Additional Monitoring:**
Bounce Rate on Launch Day · Time-to-First-20-Reviews · Review Longevity (30/60/90d) · Seeding Campaign Retention · Reviewer Pool Fatigue Rate

### Top 4 Risks

| סיכון | מיטיגציה |
|--------|----------|
| Logistics Delays | AI מפעיל backup reviewers אוטומטית |
| Review Bias (5★ trend) | AI מגביר משקל שאלות ביקורתיות בקמפיין הבא |
| FTC Violation | Disclosure Badge חובה ולא ניתן להסרה |
| Platform Gap (SFCC, Magento) | **MVP = Shopify**, Phase 2 = SFCC + Magento |

---

## סליד 11: Part 2: Microsoft Banking: Context & Why Now

### המשימה (0-to-1)

הובלת פיתוח של פלטפורמת אוטומציה דיגיטלית חדשה ל-Loan Origination בבנקים: **היישום הראשון של Microsoft Cloud for Financial Services**.

### ה-"Why Now": Trigger אסטרטגי + תפעולי משולב

**לחץ אסטרטגי מלמעלה:**
- **לחץ תחרותי:** Salesforce Financial Services Cloud כבר השיגה אחיזה אצל בנקים מובילים
- **הזדמנות בבסיס לקוחות:** בנקים שהריצו Azure + Office 365 + Dynamics 365: מורכבות אינטגרציה נמוכה משמעותית מפתרון multi-vendor (AWS + Salesforce)
- **לוגיקה אסטרטגית:** העמקת אחיזת Microsoft בלקוחות פיננסיים קיימים: באמצעות יכולות בנקאיות native על פלטפורמות שהם כבר מכירים

**דחיפות תפעולית מלמטה: שוק הקורונה:**
- **סגירת סניפים פיזיים:** ממשלות ברחבי העולם הורו על סגירת סניפי בנקים. לקוחות לא יכלו להיכנס פיזית להגיש בקשות הלוואה.
- **הגבלות התקהלות:** גם כאשר חזרו לפעילות חלקית, כללי הריחוק החברתי הגבילו את הקיבולת בסניפים לחלק קטן מהנפח הרגיל: והפכו את הליך ההגשה הפיזי לבלתי-ישים תפעולית.
- **מנוע ההכנסות נעצר בן לילה:** Loan Origination הוא אחד מקווי ההכנסות המשמעותיים של בנקים קמעונאיים. עם חסימת הערוץ הפיזי, הבנקים עמדו מול פער קיומי: איך להמשיך להפיק הלוואות ללא מגע פיזי.
- **טרנספורמציה דיגיטלית שתוכננה לטווח ארוך הפכה לציווי הישרדותי דחוף.** מה שהיה "Digital Transformation Initiative" הפך למצב חירום ברמת דירקטוריון.

**ההזדמנות נוצרה מההצטלבות:** החזון האסטרטגי והלחץ התחרותי דחפו לכיוון הזה כבר שנים: הקורונה הייתה הטריגר שהפך את ה-Digital Loan Origination לציווי הישרדותי מיידי לבנקים, לא לשאיפה ארוכת-טווח. שני הכוחות נפגשו, וחלון ההזדמנויות נפתח.

### הבעיה הליבתית

תהליך הלוואה ידני → CRM backlogs כבדים + Application Abandonment של 20-30% + Margin Erosion. תוכנות off-the-shelf נחסמו מבחינת רגולציה (Zero-Retention, Data Isolation).

---

## סליד 12: Part 2: The Hard Choice

### Architecture Trade-off

|  | **Option A: Standalone App** | **Option B: Power Platform + Teams ✓** |
|---|---|---|
| **Pros** | חופש עיצוב מלא | יורש את Trust + Compliance של Microsoft שאושרו אצל הבנקים |
| **Cons** | 12-18 חודשי compliance per bank: הורג Time-to-Market | מגבלות UX מסוימות של Teams |

### הבחירה הארכיטקטונית

בנינו על **Microsoft Power Platform** (Power Apps + Power Automate), עטפנו ב-**Microsoft Teams**.

### ה-Data Points מאחורי ההחלטה

**Data Point אסטרטגי: זמן Compliance:**
> *"הבנקים כבר סמכו על Azure, Office 365, ו-Dynamics 365: מערכות שעברו ביקורות אבטחה ו-compliance מעמיקות במשך שנים. בנייה עצמאית הייתה דורשת לחזור על התהליך עם כל בנק: 12-18 חודשים נוספים. עם Salesforce ברקע: לא יכולנו להרשות לעצמנו את העיכוב הזה."*

**Data Point תפעולי: הגילוי בשטח:**
> *"מחקר המשתמשים שלנו חשף שכל תיק הלוואה נתקע ב-3-4 סבבים של ping-pong (Rework Loops) בין הבנק ללקוח: בגלל טעויות הקלדה, חתימות חסרות ומסמכים משובשים. זה יצר עומס ידני אדיר על אנליסטים ומתח את משך המחזור על פני ימים רבים. בנייה מותאמת לכל בנק הייתה משאירה את הכאב התפעולי הזה ללא פתרון בדיוק בחודשים הארוכים ביותר של משבר הקורונה. Power Platform + Teams אפשרו לנו להשיק זרימת עבודה לביטול ה-Rework מספר בנקים במקביל: תוך טיפול בו-זמני בדחיפויות האסטרטגיות והתפעוליות."*

### למה זה עבד בפועל

- בנקים פרסו בתוך **1-3 חודשים** במקום תהליך שיכל לקחת **שנה ויותר**
- צוותים פנימיים השתמשו ב-Teams שהם הכירו: אפס curve למידה
- Power Platform's low-code אפשרה איטרציה מהירה על תהליכי החיתום

---

## סליד 13: Part 2: Results & KRs

### Key Results

| יעד | Key Result + השפעה בפועל |
|------|---------------------------|
| **Compress Loan Cycle Time** | **30-35% הפחתה במשך מחזור הלוואה**: נמדד בתחילה עם ה-Design Partner ב-Phase 1, ולאחר מכן נצפה גם בלקוחות נוספים. אוטומציית איסוף מסמכים + חיתום + ניתוב אישור. |
| **Reduce Application Abandonment** | **Baseline: 20-30%** · **Target Phase 1: <5%** · **Actual: 3% הושג.** <br><br>**למה ה-3% משמעותי: Upfront Filtering כבחירת עיצוב אסטרטגית:** בנקים מסורתית גוררים מבקשים לא-מתאימים עמוק לתוך החיתום הידני: רק כדי לדחות אותם לאחר ימי עבודה, או לגרום להם להתייאש ולעזוב. זה מבזבז קיבולת של אנליסטים ופוגע באמון הלקוחות.<br><br>המערכת שלנו הפכה את הדפוס: **סינון התאמה מתבצע דיגיטלית בכניסה למשפך**, לפני כל עבודת חיתום כבדה. מבקשים שלא היו מתאימים הופנו בצורה מכובדת מוקדם; אלה ש*כן* נכנסו לתהליך הדיגיטלי השלימו אותו בסבירות גבוהה: בתמיכת שקיפות סטטוס בזמן אמת, איסוף מסמכים דיגיטלי, וביטול הצורך בהגעה פיזית לסניף.<br><br>ה-3% הוא לא רק חוויה חלקה: זו **ארכיטקטורת משפך חכמה יותר.** |
| **Microsoft Customer Base Leverage** | פנייה ממוקדת לבנקים שהריצו Azure + O365 + Dynamics 365: מורכבות אינטגרציה נמוכה דרמטית מ-multi-vendor. **המוצר הוגדר כ-Pioneer Application של Microsoft Cloud for Financial Services**: האימות המסחרי הראשון של אסטרטגיית ה-Vertical Cloud. |

---

## סליד 14: Sources

### Research & Citations

**Problem Statement:**
- PowerReviews: *"Survey: The Ever-Growing Power of Reviews"* (2021)
  https://www.powerreviews.com/power-of-reviews-survey-2021/
- Spiegel Research Center, Northwestern: *"How Online Reviews Influence Sales"*
  https://spiegel.medill.northwestern.edu/how-online-reviews-influence-sales/
- FTC: *Trade Regulation Rule on Use of Consumer Reviews and Testimonials* (Aug 2024)
  https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials

**Competitive Landscape:**
- Yotpo Reviews Platform: https://www.yotpo.com/platform/reviews/
- Bazaarvoice Sampling: https://www.bazaarvoice.com/products/sampling/
- Amazon Vine Program: https://www.amazon.com/vine/

**Pricing Benchmark:**
- Vendr Marketplace (Bazaarvoice): https://www.vendr.com/marketplace/bazaarvoice

---

## הערות לעצמך לפני הצגה (לא במצגת)

**ניהול זמן (50 דקות):**
- חלק 1: ~35 דקות (10 סליידים = 3.5 דקות בממוצע)
- חלק 2: ~10 דקות (3 סליידים = 3.3 דקות)
- Q&A buffer: 5 דקות

**טיפים:**
- אל תקרא מהסליד. הסליד הוא רמז: לא תסריט.
- כשאתה מציג מספרים: תאט. תן להם לרשום.
- כשמראיין שואל "מאיפה המספר?": תפתח ישר את סליד ה-Sources.
- אל תיכנס לעומק טכני אלא אם נשאלת. שמור את העומק ל-Q&A.

**שאלות סבירות מהמראיין + תשובות מוכנות:**

1. *"מה ה-pricing model של Ignite?"*
   → "Ignite Basic: Bundled לכל לקוח Reviews. Ignite Pro נפתח בחינם כשיש למרצ'נט גם Reviews וגם Loyalty: Cross-Sell טבעי.
   **חלופת monetization:** למרצ'נטים שנעולים ב-Loyalty vendor מתחרה (Smile.io, LoyaltyLion): Ignite Pro זמין כ-paid add-on עצמאי ל-Yotpo Reviews. תמחור סופי TBD post-MVP בהתאם ל-willingness-to-pay validation: אבל העיקרון: לא משאירים כסף על הרצפה."

2. *"כמה זמן לבנות MVP?"*
   → "Phase 1 (Shopify-only): ~12 שבועות. Phase 2 (SFCC + Magento): ~6 חודשים נוספים."

3. *"מה אם הסוקר מקבל מוצר רע ונותן ביקורת רעה?"*
   → "Ignite לא חוסם ביקורות שליליות: הוא רק חוסם ביקורות שאינן עומדות באיכות. ביקורת רעה איכותית תפורסם. זה ה-Integrity Guardrail."

4. *"איך אתה יודע ש-Ignite Agent יבחר את הסוקרים הנכונים?"*
   → "Ignite מתבסס על דאטה היסטורית של Review Richness Score שמוכחת. בנוסף: המרצ'נט רואה את הרשימה ומאשר ידנית עם הסבר AI לכל סוקר."

5. *"מה ה-data point ב-Part 2?"*
   → ראה Slide 12. הגילוי התפעולי: 3-4 rework loops לתיק הלוואה: הוא המספר הקונקרטי. בשילוב עם 12-18 חודשי compliance, זה היה trade-off כמותי, לא רק איכותי.

6. *"מה לגבי מותגי Enterprise עם מוצרים יקרים (מזרנים, אלקטרוניקה)? האם תמריץ 'מוצר חינם' עדיין עובד?"*
   → "למוצרים יקרים, התמריץ משתנה. Layer 1 יכול להפוך ל-Early Access (VIP launch event פרטי, חבילה אקסקלוסיבית) במקום פריט פיזי חינם. Layer 2 יכול להפוך לערך gift card גבוה יותר. Ignite Agent ניתן להגדרה לפי מרצ'נט כדי לקבוע את כלכלת התמריצים לפי COGS המוצר."

7. *"איפה ה-AI באמת חיוני לעומת איפה לוגיקה פשוטה תספיק?"*
   → "לוגיקה פשוטה מטפלת בפילוח tier וזכאות בסיסית. ה-AI חיוני בשלושה מקומות:
   (a) **Review Richness Scoring**: ניתוח איכות טקסט של ביקורות עבר דורש NLP, לא חוקים
   (b) **אימות אותנטיות ויזואלי**: הבחנה בין תמונות אמיתיות של משתמשים לתמונות stock
   (c) **זיהוי דפוסי ביטול**: איתור התנהגות ביטולים חשודה על פני קמפיינים
   אלה דורשים זיהוי דפוסים, לא חוקים דטרמיניסטיים: וזו הסיבה שה-Ignite Agent קיים."

8. *"מה לגבי מוצרים שאי אפשר לשלוח חינם, תכשיטים יוקרתיים, מוצרי לבן כבדים, רהיטים?"*
   → "שאלה מצוינת. המודל של MVP, 'Free Product Drop', מתאים לבסיס הליבה של Yotpo (D2C, Fashion, Beauty, CPG, מוצרי בית קטנים). לקטגוריות לא-שילוחיות, Ignite יציע 'Reviewer Experience Types' חלופיים שהמרצ'נט יוכל לבחור פר קמפיין:
   (a) **Loaner Program** למוצרי לבן ורהיטים (השאלה ל-X ימים, החזרה אחרי)
   (b) **Showroom / Demo Visit** לתכשיטים יוקרתיים או רכבים (אירוע VIP פרטי, חוויה בחנות, ביקורת מבוססת התנסות)
   (c) **Concierge Experience** למותגי לייפסטייל פרימיום (סטיילינג פרטי, fitting, שירות)
   (d) **Early-Buy + Refund** למוצרים אולטרה-יוקרתיים (רכישה אמיתית עם החזר מלא אחרי ביקורת)
   אלה Out-of-Scope ל-MVP, אבל הרחבה טבעית ל-Phase 2/3 ששומרת על הרלוונטיות של Ignite בכל ספקטרום ה-eCommerce."
