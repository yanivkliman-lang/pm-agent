# Part 1 — Sections 3 & 4 (Draft for Review)

---

## 3. The Solution: Yotpo Ignite — The AI-Driven Seeding Engine

### 3.1 Feature Overview

Yotpo Ignite is a native, AI-orchestrated campaign module embedded directly within the Yotpo Reviews dashboard. It enables merchants to proactively build a "Day Zero" social proof layer by intelligently identifying their most qualified reviewers, automating product fulfillment, and collecting high-quality, FTC-compliant reviews — all before a product goes live.

The engine is powered by the **Yotpo Ignite Agent**, an internal AI agent that connects three existing Yotpo data assets into a single closed-loop workflow:

- **Yotpo Reviews** — Historical review data, including Review Richness Scores (text length, photo/video inclusion, sentiment depth) per customer
- **Yotpo Loyalty** — Tier membership, LTV, engagement frequency, and points balance per customer
- **Shopify Catalog** — Product metadata including category, tags, description, and attributes of the upcoming product

No new data infrastructure is required. Ignite surfaces intelligence that already exists within the Yotpo ecosystem.

---

### 3.2 How a Merchant Initiates a Seeding Campaign (The Merchant Flow)

The campaign workflow follows a **T-Minus 14-day minimum timeline** from campaign creation to launch day. 14 days is both the minimum and the recommended default — merchants can extend the timeline up to 30+ days when planning a larger drop. Shorter timelines may be explored in a future phase based on customer feedback and shipping-partner integrations, since real-world delivery can take anywhere from 2 days to a full week depending on the destination.

---

**Step 1 — Campaign Setup**
`T-Minus 14 Days`

The merchant opens the Yotpo dashboard and clicks **"Create Seeding Campaign."** They:
- Connect the upcoming Product ID (currently in "Draft" status in Shopify)
- Set the target launch date
- Define the target reviewer pool size (default: 35 reviewers → expected yield: ~30 approved reviews based on 85% industry submission rate)
- Set the review embargo date (T-0: launch day)

---

**Step 2 — AI Product Scan**
`Real-Time`

The Ignite Agent scans the product's draft page — analyzing title, description, category, tags, and images — to build a semantic product profile.

*Example: "Trail running shoe, waterproof membrane, lightweight, size-inclusive" → mapped to attributes: comfort, fit accuracy, waterproofing, durability.*

---

**Step 3 — Cross-Database Reviewer Matching**
`Real-Time`

The Ignite Agent queries the merchant's unified Yotpo database and scores every customer across two dimensions:

| Signal | What It Measures |
|--------|-----------------|
| **Category Affinity** | Did this customer historically purchase and review products in the same category? |
| **Review Richness Score** | Does this customer write long-form reviews with photos? (Top 10% threshold) |
| **Loyalty Tier** | Is this customer in the top loyalty tier — indicating brand affinity and reliability? |
| **Review Recency** | Has this customer written a review in the past 90 days? |

The output is a ranked **Seeding Pool** of the 35 best-matched reviewers for this specific product.

---

**Step 4 — Merchant Approval**
`T-Minus 13 Days`

The merchant reviews the proposed Seeding Pool in a clean dashboard view — showing each reviewer's name, loyalty tier, past review count, and average Review Richness Score. The merchant approves with one click or manually swaps specific reviewers.

---

**Step 5 — Reviewer Opt-In & Automated Fulfillment**
`T-Minus 13 Days`

Before any product is shipped, each selected reviewer receives an opt-in message via **SMS / Email / WhatsApp**:
> *"Hi Sarah! [Brand] is dropping something exclusive next week and you're on the shortlist. Want early access? Reply YES to join."*

Only reviewers who actively confirm participation proceed to fulfillment. This ensures genuine willingness — not passive inclusion.

Upon opt-in confirmation:
- Ignite Agent generates **$0 draft fulfillment orders** directly in Shopify for each confirmed reviewer — no manual shipping required
- Products are shipped via the merchant's standard logistics partner
- The Ignite Agent monitors delivery tracking in real-time via **Carrier Delivery Webhook** (integrated with Shippo / AfterShip)

Upon confirmed delivery, the review link is sent automatically:
> *"Your exclusive preview just arrived! Here's your personal review link: [link]. You have 5 days to share your honest experience and earn your VIP points."*

- **Day 3 post-delivery** (if no submission): Reminder with direct review link
- **Day 5 post-delivery:** Final reminder — "Last chance to share your review and earn your VIP points."

> **Note:** The review link is sent only upon delivery confirmation webhook — never in advance. This ensures the reviewer has physically received the product before being asked to review it.

---

**Step 6 — Review Submission via Smart Review Form**
`T-Minus 10 Days to T-Minus 2 Days`

Each reviewer submits through a dedicated **Smart Review Form** (see Quality Control section below). Reviews are collected and held in **"Pending — Embargoed"** status, invisible to the public.

---

**Step 7 — The 24-Hour Lock Window**
`T-Minus 24 Hours`

All approved, high-quality reviews are locked, validated by the Ignite Agent, and scheduled for automatic publication at the exact moment the product goes live on the storefront.

> **Design Decision — Merchant Visibility & Control:**
> The merchant **can read all collected reviews** before confirming the launch. However, they **cannot selectively suppress individual reviews** based on rating or sentiment.
>
> The merchant has two options at this stage:
> 1. **Confirm Launch** — all approved reviews go live at T-0
> 2. **Cancel Campaign** — if the overall review quality is unacceptable, the merchant can cancel the entire campaign. This action is logged in a transparent audit trail for FTC compliance purposes.
>
> This model gives merchants the visibility they need to trust the process, while preventing cherry-picking of positive reviews only. The Ignite Agent approves individual reviews based solely on quality thresholds (150+ characters + verified photo) — never on rating or tone.

The merchant sees: *"28 of 30 target reviews ready for launch. Average rating: 4.6★"* — reads through the reviews — and confirms launch with one click.

At T-0, reviews go live simultaneously with the product — instantly syndicated to Google Shopping, Meta, and retail partners via Yotpo's existing syndication infrastructure.

---

### 3.3 The Reviewer Incentive: The Double Incentive Model

To ensure high participation and submission quality, Ignite employs a two-layer incentive structure rooted in Yotpo Loyalty economics:

**Layer 1 — The Free Product Drop (Immediate Incentive)**
The reviewer receives the product entirely free, before anyone else can buy it. For loyalty-driven customers of aspirational brands (e.g., beauty, streetwear, fitness), this is not merely a discount — it is **Insider Status**: a signal from the brand that they are trusted and valued above the general public.

**Layer 2 — VIP Review Points (Loyalty Incentive)**
Upon the Ignite Agent's verification that the submitted review meets quality thresholds (minimum character count + photo/video), the system automatically deposits **VIP Bonus Points** into the reviewer's Yotpo Loyalty account. These points carry real monetary value redeemable on future purchases (e.g., equivalent to a $15–$20 store credit).

**Gamification & Accountability (3-Strike Rule)**
To maintain pool integrity without damaging brand relationships:
- A reviewer who fails to submit within the 5-day window receives Strike 1 — they are deprioritized in future campaigns
- After Strike 2 — they are moved to a lower reviewer tier
- After Strike 3 — they are removed from the Seeding Pool entirely

This graduated system protects the merchant's VIP relationships while maintaining campaign reliability.

**Exception — Product Issue Reporting:**
If a reviewer receives a defective product or an incorrect size, they can tap **"Report a Product Issue"** directly within the review flow. This freezes the strike clock, triggers an automatic customer service alert to the merchant, and allows the reviewer to either receive a replacement or exit the campaign gracefully — with no penalty to their reviewer standing.

> **FTC Compliance (Built-In):** Every review collected via Ignite is automatically published with a transparent **"Received free product as part of a brand seeding program"** badge — compliant with FTC's 2024 Consumer Reviews and Testimonials Rule.

---

### 3.4 Quality Control: The Smart Review Form

When a reviewer clicks the review link, they enter a dynamic review form engineered for richness, not just completion.

**Dynamic Attribute Prompts**
The Ignite Agent knows the product's key attributes and generates specific, guided questions the reviewer must address:
> *"How did the shoe's sizing compare to your usual size?"*
> *"Did the waterproofing perform as expected in wet conditions?"*

These prompts produce attribute-rich, useful reviews — not generic "great product!" submissions.

**Visual Enforcement**
Submission is blocked until the reviewer uploads at least one photo or short video of the physical product. The Ignite Agent performs a basic image scan to reject:
- All-black or blank images
- Screenshots
- Stock imagery (reverse image search validation)

**Real-Time Quality Meter**
A live character counter and quality progress bar guides the reviewer toward a minimum of **150 characters**. The form labels this as *"Review Quality Score"* — making it feel like a personal achievement rather than a compliance requirement.

---

### 3.5 Edge Case: The Cold-Cold Start

**Scenario:** A merchant launches an entirely new product category with no historical purchase or review data in that category.

*Example: A fashion brand launching its first skincare line — no customer has ever bought skincare from this store.*

**How Ignite Handles It — Behavioral Segmentation Mode:**

When the Ignite Agent cannot find sufficient category-affinity matches, it switches to **Behavioral Segmentation**: identifying customers who are chronic, high-quality reviewers regardless of category — customers who love writing and love being photographed with products.

To validate real-world relevance, the Ignite Agent triggers a **Micro-Survey Switch**: an automated single-question SMS to the top 200 loyalty members:

> *"Hey Sarah, we're dropping something new and secret this week. Do you use SPF moisturizer daily? Reply YES to be considered for an exclusive free preview."*

Responses are processed in real-time. Customers who reply "YES" are instantly elevated to the campaign's Seeding Pool, despite having no skincare purchase history on the store.

This approach maintains reviewer authenticity (real category users) while bypassing the cold-data limitation.

---

## 4. Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|-----------|
| 1 | **Logistics bottleneck** — Shipments delayed; insufficient reviews ready at T-24 | Medium | High | Real-time logistics risk dashboard alerts merchant when ≥3 shipments are delayed. Ignite automatically activates backup reviewers from a pre-approved waitlist |
| 2 | **FTC violation** — Reviewer fails to disclose free product receipt | Low | Critical ($51,744 per violation) | Disclosure badge is system-enforced and non-removable. Reviewer must check a mandatory disclosure checkbox before submitting |
| 3 | **Review bias** — Free product recipients trend toward 5-star ratings, reducing perceived authenticity | Medium | Medium | "VIP Product Seeding" badge sets consumer expectations. Ignite tracks average seeded review rating vs. organic review rating; alerts merchant if gap exceeds 0.8 stars. If the gap persists across two consecutive campaigns, the Ignite Agent automatically increases the weight of critical-attribute questions in the Smart Review Form — prompting reviewers toward more balanced, specific feedback rather than generic praise |
| 4 | **Reviewer pool fatigue** — Same VIPs targeted across multiple campaigns, reducing response rates | Medium | Medium | Enforced cooldown: no reviewer can participate in more than 2 campaigns within 90 days. Pool Health dashboard flags fatigue risk |
| 5 | **Merchant gaming** — Merchant attempts to use Ignite for fake reviews on existing products | Low | High | Ignite is gated to products in "Draft" or "Pre-launch" Shopify status only. Cannot be activated on live products |
| 6 | **Cold-Cold Start failure** — Micro-Survey response rate too low to fill the pool | Low | Medium | If confirmed pool falls below 20 reviewers at T-10, merchant is alerted and can choose to: (a) delay launch, (b) reduce pool target, or (c) open campaign to a broader loyalty tier |
| 7 | **New merchant with no review history** — Ignite Agent has no data to score reviewers | Medium | Medium | For merchants with <6 months of Yotpo data, Ignite switches to Loyalty-tier-only segmentation (top 10% by spend) as a baseline signal, with a disclaimer that pool quality improves over time |
| 8 | **Platform compatibility gap** — Ignite's fulfillment automation relies on Shopify's native Draft Order and Draft Product status APIs. Enterprise merchants on Salesforce Commerce Cloud (SFCC) or Magento do not have an equivalent "Draft" product state and require custom API middleware to generate $0 fulfillment orders | Medium | Medium | **MVP scope is explicitly Shopify.** SFCC and Magento merchants will be supported in a Phase 2 release via a dedicated API connector layer. This should be communicated clearly at onboarding to avoid expectation gaps with enterprise sales prospects |
