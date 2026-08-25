# MathQuest: Project Requirements Document (PRD)

## 1. Executive Summary
**MathQuest** is an AI-native educational ecosystem designed to teach mathematics to learners ranging from toddlers (párvulos) to advanced students. The platform leverages a 3D Claymation aesthetic to provide a tactile, high-visibility interface suitable for both young children and seniors with visual impairments.

## 2. Product Vision & Goals
- **Objective:** Democratize math education through a multi-platform (Web, Android, Desktop) experience.
- **Key Philosophy:** "Solve the Impossible" through the CPA (Concrete-Pictorial-Abstract) methodology.
- **Core Requirement:** Forced progression starting from the most basic levels (1, 2, 3) for all users without exception.

---

## 3. Pedagogical Framework
### 3.1. CPA Methodology
1.  **Concrete:** Interactive 3D objects representing quantities.
2.  **Pictorial:** Visual representations (e.g., drawings or icons).
3.  **Abstract:** Introduction of symbols (1, 2, 3, +, =, etc.).

### 3.2. Learning Trajectories
- **Subitizing:** Recognizing small quantities instantly.
- **One-to-One Correspondence:** Linking physical interaction with numerical counting.
- **Faded Scaffolding:** Gradually reducing visual aids as the student demonstrates mastery (3-repetition cycle).

---

## 4. Technical Architecture
### 4.1. Frontend
- **Framework:** Next.js (React) for SEO and performance.
- **Styling:** Tailwind CSS with the "Luminous Equation" design system.
- **Animation:** Framer Motion and Three.js for interactive 3D elements.
- **Interface Design:** "Jumbo" interactions—large, high-contrast buttons for accessibility.

### 4.2. Backend (BaaS)
- **Core:** Supabase (PostgreSQL).
- **Key Tables:**
    - `profiles`: XP, levels, and student metadata.
    - `progress_logs`: Mastery tracking with RLS (Row Level Security).
    - `tutor_settings`: Linkage between parent/educator and student.
- **Authentication:** Email/Password (Tutors) and OAuth (Google/Apple).

### 4.3. Infrastructure & Deployment
- **Hosting:** High-capacity providers (Vercel/Netlify) to handle heavy assets.
- **Security:** Cloudflare for DDoS protection, SSL/TLS, and WAF rules against SQLi/XSS.
- **Offline Support:** Service Workers for basic level access without connectivity.

---

## 5. User Roles & Experience
### 5.1. The Learner (Child)
- **Entry Point:** Level 1 (Number identification).
- **Reward System:** Positive visual reinforcement (notorious smiling faces) and XP accumulation.
- **Cycle:** 3 successful repetitions required to clear a module.

### 5.2. The Tutor (Adult)
- **Parental Gate:** Challenges (e.g., "8x7+15") required to access settings or payments.
- **Dashboard:** Access to pedagogical justifications and detailed progress reports via the "Tutor Panel."

---

## 6. Monetization Strategy
- **Model:** Freemium (SaaS).
- **Gateway:** Stripe Billing & Checkout (PCI compliant).
- **Subscription Levels:**
    - *Free:* Basic numbers (1-10) and operations.
    - *Premium (Explorer):* Advanced symbols (π, λ), algebra, and multi-child profiles.

---

## 7. Marketing & Growth
- **Channel Strategy:** TikTok/Reels focusing on high-quality 3D animations (Claymation style).
- **Asset Focus:** "Jumbo Interaction" videos and character-driven jumping animations (Squash & Stretch principles).

---

## 8. Implementation Roadmap (Phase 1)
- [x] Design System (Luminous Equation).
- [x] Basic Mastery Levels (1-5).
- [x] Tutor/Admin Backend Screens.
- [x] Data Architecture (Supabase).
- [x] Deployment Manuals.
- [ ] Level 6-10 Development (Upcoming).
- [ ] Sums & Basic Arithmetic.
- [ ] Global Leaderboard Implementation.

---
**Version:** 1.0
**Project Lead:** Stitch AI Designer
**Design System ID:** {{DATA:DESIGN_SYSTEM:DESIGN_SYSTEM_1}}
