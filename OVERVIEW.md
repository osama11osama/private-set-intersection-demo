# Project Overview & Real-World Use Cases

> A plain-language guide to what this project does, why it matters, and where similar ideas appear in the real world.  
> **No math. No code. No cryptography jargon required.**

For technical details, protocol steps, and implementation, see the [main README](README.md).

---

## Table of Contents

- [The Big Idea](#the-big-idea)
- [Everyday Example](#everyday-example)
- [How This Project Demonstrates It](#how-this-project-demonstrates-it)
- [Why Not Just Share the Lists?](#why-not-just-share-the-lists)
- [Real-World Use Cases](#real-world-use-cases)
- [From Classroom Demo to Real Product](#from-classroom-demo-to-real-product)
- [Further Reading](#further-reading)

---

## The Big Idea

Imagine two people — or two companies — each holding a **private list** of items: phone numbers, account IDs, email addresses, or any identifiers.

They want to answer one simple question:

> **“What do we have in common?”**

Without either side handing over their **full list** to the other.

That is the core idea behind **Private Set Intersection**. This project implements a related variant: one side holds a large list, and the other side asks, **“Is my item on your list?”** — again, without exposing everything else.

Think of it as a **privacy-preserving overlap check**.

---

## Everyday Example

**Alice** runs a messaging app. She has a contact list of 500 phone numbers on her phone.

**Bob** runs the app’s servers. He knows which phone numbers are registered on the platform — thousands of them.

Alice wants to know: *“Which of my contacts already use the app?”* so she can suggest them as friends.

**What she does not want:** to upload her entire contact book to Bob’s servers in plain text.

**What Bob does not want:** to send Alice his full user database.

A private intersection protocol lets them discover **only the matches** — the numbers that appear on **both** sides — while keeping everything else hidden.

---

## How This Project Demonstrates It

In our demo:

- One party (**Receiver**) holds a fixed list of numbers — like a private database.
- Other parties (**Senders**) each enter their own small lists.
- The protocol checks whether any of the sender’s numbers appear in the receiver’s list.
- When there is a match, the program reports it. When there is not, the non-matching numbers stay private.

It is a **simplified teaching version** of ideas used in real privacy technology — built for a university cybersecurity course, not for production deployment.

---

## Why Not Just Share the Lists?

| Approach | Problem |
|----------|---------|
| Send your full list to the other party | They see everything — contacts, customers, suspects, patients |
| Hash the list and compare hashes | Still vulnerable if the data is predictable (e.g. phone numbers) |
| Use a trusted middleman | Someone else holds all the data — single point of failure and trust |
| **Private intersection** | Only shared items are revealed; the rest stays with each owner |

Privacy laws (GDPR, HIPAA, and similar regulations), competitive concerns, and basic trust all push toward solutions where **less data is exposed**, not more.

---

## Real-World Use Cases

Below are areas where the **same underlying idea** — finding overlap without full disclosure — is used or actively researched.

### Contact discovery

**Who:** Messaging apps (e.g. Signal-style contact discovery)

**Question:** “Which of my contacts are on this service?”

**Why privacy matters:** Users should not have to upload their entire address book in readable form.

---

### Advertising and analytics

**Who:** Advertisers and platforms measuring ad effectiveness

**Question:** “How many people who saw our ad actually made a purchase?”

**Why privacy matters:** The advertiser learns a **count** or **overlap**, not every customer’s full browsing or purchase history from the other side.

---

### Cybersecurity and fraud

**Who:** Banks, insurers, security teams

**Question:** “Do we share any flagged account IDs, IP addresses, or threat indicators?”

**Why privacy matters:** Institutions can cooperate against fraud and attacks **without** sharing their entire customer or threat databases.

---

### Healthcare and research

**Who:** Hospitals, research networks

**Question:** “Do our patient cohorts overlap for this study?”

**Why privacy matters:** Researchers can find common cases **without** exchanging full medical records unnecessarily.

---

### Compliance and sanctions screening

**Who:** Banks, fintech, international trade

**Question:** “Is this person or company on a restricted list?”

**Why privacy matters:** The querying party gets a **yes/no** (or match result), not a copy of the entire sanctions database.

---

### Government and intelligence (with strict policy)

**Who:** Agencies sharing watchlists under legal frameworks

**Question:** “Do our suspect lists overlap?”

**Why privacy matters:** National laws and treaties often **forbid** bulk data sharing; intersection-only protocols align better with those rules.

---

### Password breach checking

**Who:** Password managers, browsers (“Have I been pwned?” style services)

**Question:** “Has this password appeared in a known breach?”

**Why privacy matters:** The user should not send their actual password in clear text; private membership checks are a natural fit.

---

## From Classroom Demo to Real Product

Our project is a **learning implementation**. Moving to a real-world product would require, among other things:

- Stronger security parameters and expert review
- Running the two parties over a network with authentication and encrypted transport
- Clear legal and policy frameworks (especially for sensitive domains)
- Often, adopting **mature open-source PSI libraries** rather than a custom protocol alone

The **concept** is production-relevant. This **specific codebase** is a starting point for understanding, not a drop-in solution for a bank or hospital.

---

## Further Reading

| Document | Contents |
|----------|----------|
| [README.md](README.md) | Technical overview, protocol flow, installation, API, security notes |
| Repository source | `Run_Protocol.py`, `Sender.py`, `Receiver.py`, `utils.py` |

---

<p align="center">
  <sub>Project_PCI — CySec course project, Saarland University, 2020</sub><br>
  <sub>Authors: Abdullah Malallah · Osama</sub>
</p>
