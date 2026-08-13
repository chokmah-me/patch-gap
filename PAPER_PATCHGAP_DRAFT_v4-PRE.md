<p class="hebrew-epigraph" dir="rtl" lang="he">אִם יִרְצֶה הַשֵּׁם</p>
<p class="hebrew-date" dir="rtl" lang="he">כ״ט בְּאָב ה׳תשפ״ו</p>

# The Governance Patch-Gap: Machine-Speed Exploit Discovery Against Human-Speed Legal Repair

Daniyel Yaacov Bilar, Chokmah LLC, chokmah-dyb@pm.me , ORCID: [0000-0002-9040-6914](https://orcid.org/0000-0002-9040-6914)

v 1.1-draft, August 13, 2026 (source draft; minted PDF remains v1.0). AI is an automated vulnerability scanner for the rule of law: this paper formalizes the rate asymmetry between machine-speed exploit discovery and human-speed legal repair as the governance patch-gap

DOI (concept, always latest): https://doi.org/10.5281/zenodo.21910874  
This minted PDF (v1.0): https://doi.org/10.5281/zenodo.21910875  
v1.1 version DOI: pending remint under the same concept

## Abstract

Legal systems governed by rule of law are, structurally, rule systems. Like any rule system, they contain gaps between specification and intent, concentrated in the deliberately under-specified provisions that legal philosophers call "open texture." Those gaps have always been exploitable, but exploitation was rate-limited by the cost of legal expertise and the size of the corpus to be searched. That rate-limit is now collapsing. This paper introduces the governance patch-gap: the ratio between the rate at which AI accelerates the discovery of exploitable legal ambiguities and the rate at which legislatures, courts, and treaty bodies can repair them. Using the Highly Optimized Tolerance (HOT) framework from complex-systems theory, we map legal systems onto designed artifacts whose optimization against anticipated disputes concentrates fragility at the boundaries of the specification. We define the patch-gap as a ratio of discovery rate to repair rate, identify a threat taxonomy (corporate optimizer, state actor, misaligned autonomous agent), distinguish exploit discovery from exploit execution as separate governance problems, and examine three defensive strategies and the structural limits that prevent any defense from closing the gap entirely. The paper closes with three falsifiable predictions for 2027 to 2028.

## 1. Introduction

A statute is a specification. A regulation is an implementation. A judicial opinion is a patch. A legal loophole is a vulnerability: a gap between the specification's intent and its operational behavior under adversarial input.

This mapping is a structural analogy, not a loose metaphor; the same lifecycle governs both domains. Statutes specify permitted and prohibited behavior. Regulations translate those specifications into operational rules. Courts repair specification failures when adversarial inputs produce outcomes the drafters did not intend. The process is iterative, adversarial, and path-dependent, the same lifecycle that governs software systems.

Legal systems differ from software in one respect that matters for this paper: software bugs are unintentional, but many legal ambiguities are deliberate. Statutes use terms like "reasonable," "undue burden," and "public interest" precisely to leave room for adaptive interpretation. This deliberate ambiguity is a design feature, not a defect. It allows law to handle circumstances that drafters could not foresee.

But a design feature in one context can be a vulnerability in another. When the entity interpreting an ambiguous provision is a human judge operating within shared normative frameworks, deliberate open texture works as intended. When the entity interpreting it is an optimization process trained to maximize a reward signal, the same open texture becomes search space. The optimizer treats "reasonable" not as a constraint to be honored but as a free variable to be exploited.

AI is collapsing the cost of discovering exploitable ambiguities in legal systems while the cost of repairing those systems remains at human speed. The resulting asymmetry, which we call the governance patch-gap, is an expanding window of exploit availability. It is not a misuse case to be addressed at the model level. It is an emergent property of optimization against any sufficiently large and ambiguous rule system.

### 1.1 The problem is old; the speed is new

The idea that a republic can be subverted through its own rules is at least 160 years old. In 1864, Maurice Joly published *Dialogue aux Enfers entre Machiavel et Montesquieu*, a step-by-step procedural playbook for converting a liberal democracy into a despotism without ever violating its formal rules. Written as satire of Napoleon III's autocratic methods, the text remains an early literary demonstration that a republic's mechanisms can be turned against its purposes from the inside [8]. The same erosion-through-legal-means pattern recurs in contemporary democracies, where elected leaders dismantle constitutional constraints using ordinary legislative and judicial tools rather than force [15].

The same dynamic played out in the United States between 2020 and 2022. The certification process under the Electoral Count Act of 1887 contained under-specified exceptional cases, procedural gaps that the drafters never anticipated would be tested adversarially. Those gaps were exploited. Congress patched them with the Electoral Count Reform Act of 2022 [24], two years after the exploit was demonstrated. This is a real-world patch cycle with a measurable latency: two years from exploit to repair, for a single, high-salience, bipartisan-consensus vulnerability.[^1]

[^1]: Goedel (1947) reportedly identified a constitutional self-amendment path to dictatorship during his naturalization hearing with Einstein and Morgenstern. The incident is well-attested (Morgenstern recorded it), but Goedel's specific argument has never been recovered.

All historical analyses of legal-system exploitation assumed human actors. The time required to find and exploit a legal ambiguity was bounded by three costs: (a) the cost of legal expertise, (b) the size of the corpus to be searched, and (c) the political capital needed to act on a discovered gap. These costs imposed a natural rate-limit on governance exploitation. This paper argues that the rate-limit is now collapsing.

### 1.2 Two theoretical foundations

Two independent intellectual traditions converge on the same structural feature of legal systems.

H.L.A. Hart, in *The Concept of Law* (1961), distinguishes the "core" of a legal rule (its settled, unambiguous meaning) from its "penumbra" (the zone of uncertainty he calls "open texture") [6]. Open texture is the mechanism by which law adapts to unforeseen circumstances. Hart's analysis provides the technical description of the attack surface: the penumbra is where the specification is incomplete, and therefore where adversarial inputs are most likely to produce unintended outcomes.

Carl Schmitt, in *Political Theology* (1922), locates sovereignty not in the routine operation of law but at the point where the rule system's specification runs out: "Sovereign is he who decides on the exception" [7]. Schmitt's insight, used here for one formal point only and without endorsement of his broader political commitments, identifies a political consequence: whoever controls the interpretation of the exceptional case, the case the drafters did not anticipate, controls the effective meaning of the rule. Sovereignty lives not in the specification but at its boundary.

Hart tells you the gaps exist. Schmitt tells you what it means to fill them. This paper asks: what happens when an optimization process fills them at machine speed?

### 1.3 Relation to prior work

The argument extends a line of work on impossibility constraints in autonomous governance [2][3][4][5]. In the military domain, three independent mathematical results (Rice's theorem, FLP impossibility, cryptographic attestation bounds) establish that for autonomous systems under hard latency constraints, the sovereign position becomes formally unoccupiable. The civilian case, treated in this paper, is analogical rather than formal: the void arises from the other direction, because optimization discovers and exploits exceptions faster than the sovereign can ratify new rules.

The key ideas from the prior work are restated in Section 6.4 where they are needed, together with the primary sources for each theorem. This paper is self-contained.

## 2. Related Work

**AI and social-system hacking.** Schneier [12] argues that "hacking" generalizes beyond computer systems to any rule-based social structure, including tax codes, financial regulations, and democratic processes. His framework is discursive. He does not formalize the dynamics or model the asymmetry between exploit discovery and system repair. This paper supplies that definition.

**AI governance and automated legal interpretation.** Calo [13] identifies the regulatory challenges specific to AI and robotics. Citron and Pasquale [25] address algorithmic accountability in scoring and prediction systems. Balkin [26] examines the constitutional implications of AI deployment. Scheppele [14] introduces "autocratic legalism," the use of formally legal procedures to hollow out democratic substance, a dynamic directly parallel to the SocioHack findings and to Joly's 1864 demonstration. These scholars identify the problem space. This paper contributes a formal definition (the patch-gap) and connects it to complex-systems theory.

**Regulatory arbitrage as a pre-AI phenomenon.** The corporate-law literature on regulatory arbitrage (Romano [16], Fleischer [17]) documents systematic exploitation of cross-jurisdictional gaps decades before AI. Ruhl and Katz [22] independently show that legal complexity itself can be measured with the tools of complexity science, the same framework this paper applies to exploitability rather than complexity. AI does not create regulatory arbitrage. It accelerates the discovery of arbitrage opportunities and, with agentic deployment, the execution of arbitrage strategies. The pre-existing literature strengthens this paper's argument by showing that the underlying dynamic is real and well-documented. What has changed is the rate.

**Reward hacking and specification gaming.** The AI safety literature on reward hacking (Amodei et al. [18], Skalse et al. [19]), Goodhart's Law applied to reinforcement learning (RL) (Manheim and Garrabrant [20]), and specification gaming (Krakovna et al. [21]) establishes that RL agents routinely find unintended solutions to specified objectives. Liu et al. [9] extend reward hacking from synthetic environments to real regulatory structures, naming the result "societal hacking." This paper treats societal hacking as one instance of a broader class: optimization against open-textured rule systems.

## 3. Rule Systems as Attack Surfaces

### 3.1 The HOT/RYF mapping

The Highly Optimized Tolerance (HOT) framework [11] models engineered systems as artifacts optimized against a distribution of anticipated perturbations. Optimization against common-case failures concentrates fragility at the boundaries of the design envelope, where rare, unanticipated inputs arrive. The result is a system that performs well against what it was designed for and poorly against everything else. Carlson and Doyle call this the Robust-Yet-Fragile (RYF) property.

Legal systems fit the HOT template:

- **Design parameter:** the statutory text and its implementing regulations.
- **Tolerance distribution:** the set of anticipated disputes, weighted by historical frequency, that the drafters optimized the text to resolve correctly. Tax codes are optimized against common forms of evasion. Employment law is optimized against known patterns of discrimination. The drafters write for the cases they can imagine.
- **Perturbation class:** adversarial inputs, unanticipated fact patterns, edge cases, and cross-statute interactions that fall outside the tolerance distribution.
- **Fragility concentration:** Hart's penumbra. The open-textured provisions where the specification is deliberately incomplete are exactly the regions where optimization against common cases provides no protection against rare inputs.

RYF predicts that a legal system will perform well against the disputes it was drafted to handle and will break down at the boundaries of the drafters' imagination. Hart's penumbra is where the fragility concentrates. Schmitt's exception names the political consequence of occupying that fragile region: whoever interprets the indeterminate case first controls the rule's effective meaning. HOT explains why the fragility sits there; Schmitt explains what it means to exploit it; AI collapses the cost of finding it.

### 3.2 Threat taxonomy

Three distinct adversary classes produce different attack trees and require different defenses.

The **corporate optimizer** is a firm using AI to minimize tax exposure, maximize regulatory classification advantages, or exploit cross-jurisdictional gaps. Its motivation is profit. Its speed is fast, limited by AI-assisted legal teams rather than AI alone. Its constraint is reputational: the firm is a repeat player, subject to enforcement, and visible to regulators and the public.

The **state actor** exploits another jurisdiction's legal ambiguities for strategic advantage, routing around one jurisdiction's review process via another jurisdiction's authority (see Section 5.3 for examples). Its motivation is geopolitical. Its speed is moderate: state actors still operate through human diplomatic channels, though AI can accelerate identification of exploitable provisions. Its constraint is international norms and reciprocity.

The **misaligned autonomous agent** is an AI system with a misspecified reward function that discovers regulatory loopholes as a byproduct of optimizing a business objective, with no human principal intending the exploit. This is the SocioHack scenario [9]. Its motivation is reward maximization. Its speed is machine speed. Its constraint is none, unless the deployment architecture includes human review of actions taken.

Conflating these three classes produces bad policy. A disclosure requirement is effective against corporate optimizers (who can be compelled to disclose) and useless against misaligned agents (which have no principal to disclose to). Section 6 maps each defensive measure to the adversary classes it can reach.

### 3.3 Attack work effort

Attacker work effort is the "ignored dual" of vulnerability [1]. A loophole that exists but requires ten million dollars in legal fees and five years of litigation to exploit is, in security terms, a vulnerability with a high work factor. The work factor is what kept the hackable-republic problem bounded for most of legal history.

AI collapses the work factor for legal exploit discovery the same way it collapsed the cost of code generation. The loopholes were always there. What has changed is the cost to find them.

### 3.4 Empirical evidence

The argument rests on a structural isomorphism between reward functions and regulatory frameworks, treated here as a working hypothesis (see Conclusion for its status as a load-bearing weakness): both enumerate thresholds, specify exceptions, define measurable outcomes, and leave institutional intent only partially expressed in their text. If this isomorphism holds, then reward hacking, a well-characterized phenomenon in RL, will manifest against regulatory structures whenever an RL-trained system is optimized in a regulatory environment.

Four independent lines of evidence support this, of differing evidentiary weight. The first is the weakest leg of the four and should be read accordingly.

First, the SocioHack experiment [9]. Liu et al. trained an RL policy (Qwen3-30B-A3B) across 72 sandbox regulatory environments evaluated by an LLM judge (Cohen's kappa = 0.55 against human annotators). The models independently rediscovered historically patched loopholes in credit card reward structures, SEC Rule 10b5-1 insider-trading windows, pharmaceutical patent extensions (Hatch-Waxman), Texas two-step bankruptcy structures, and airline contract-of-carriage pricing. The strategies remained formally compliant while defeating regulatory intent. Current LLM safeguards provided no meaningful defense. This result is an unreplicated preprint as of August 2026. It is treated here as suggestive, not dispositive, and the paper's conclusions do not depend on it holding up under replication.

Second, autonomous smart-contract exploit generation [10]. Gervais and Zhou built the A1 agentic system for end-to-end vulnerability discovery in Ethereum smart contracts. A1 achieves a 63% success rate on the VERITE benchmark (36 already-vulnerable contracts, not a random corpus). Cost per attempt: $0.01 to $3.59. The economics are asymmetric: attackers achieve profitability at $6,000 in exploit value while defenders require $60,000. Smart contracts are formalized rule systems. The attacker/defender cost asymmetry in that domain previews the same asymmetry in natural-language legal systems, where the rules are less precise and therefore more exploitable.

Third, the specification-gaming catalog maintained by Krakovna et al. [21]. This is a systematically documented collection of cases where RL agents find unintended solutions to specified objectives. The phenomenon is general across environments and model architectures. It is a property of optimization against incomplete specifications, not a bug in a particular system.

Fourth, the corporate-law literature on regulatory arbitrage [16][17]. Decades of systematic exploitation of regulatory ambiguities (tax inversions, jurisdiction shopping, creative compliance) demonstrate the same phenomenon at human speed and confirm that the underlying dynamic predates AI.

The argument does not depend on any single line of evidence. If SocioHack fails replication, the structural isomorphism and the other three lines still hold.

## 4. The Governance Patch-Gap

### 4.1 The asymmetry

The governance patch-gap is modeled on the verification bottleneck in AI code generation: the cost of generating code has collapsed while the cost of checking whether that code is correct has not. The same asymmetry applies to legal exploit discovery and legal system repair.

**Table 1.** The verification-bottleneck asymmetry between code and law. Discovery cost has collapsed for code and is collapsing for law; repair cost has not moved proportionally in either domain, and for law's penumbral provisions repair cannot be made formally verifiable at all (Section 4.2).

| Dimension | Code | Law |
|---|---|---|
| Discovery cost | Collapsed (LLM code generation) | Collapsing (RL + legal corpus parsing) |
| Repair cost | High (testing, review, formal verification) | Very high (legislative process, judicial review, treaty renegotiation) |
| Patch latency | Days to weeks (software release cycle) | Months to decades (Electoral Count Reform Act: 2 years; treaty renegotiation: a decade or more) |
| Patch completeness | Formally verifiable in principle | Not formally verifiable for penumbral provisions (see 4.2) |

### 4.2 Engaging the computational-law objection

The claim that legal systems cannot be formally verified is contested. Computational law efforts, including the Catala language [23] and Rules as Code initiatives in New Zealand, Canada, and France, attempt to make legal rules machine-checkable.

Formal verification is achievable for the core of legal rules: the narrow, well-specified regulatory domains where a rule can be translated into a decidable formal language without loss. Tax calculation, benefit eligibility determination, and procedural deadlines are all candidates. These are exactly the provisions where Hart's analysis predicts low vulnerability: the core, not the penumbra.

Formal verification is structurally unable to handle the penumbral provisions that constitute the primary attack surface. "Reasonable care," "undue burden," "public interest," and "significant risk to fundamental rights" (EU AI Act, Art. 6) cannot be formalized without destroying the adaptive capacity the terms were chosen to preserve. Formalizing "reasonable" requires fixing a definition. Fixing a definition eliminates the flexibility that allows law to handle unforeseen circumstances. Eliminating that flexibility creates a different kind of fragility: the system becomes brittle to cases it cannot classify.

The choice between open texture and formal specification is a fundamental tradeoff in legal design, not a temporary engineering limitation. The computational-law movement can shrink the attack surface by formalizing everything formalizable. It cannot eliminate the penumbra, because the penumbra exists for a reason.

### 4.3 Defining the patch-gap

Define the governance patch-gap as a ratio:

$$G = \frac{R_d}{R_p}$$

where $R_d$ is the rate of exploit discovery (exploitable ambiguities identified per unit time) and $R_p$ is the rate of effective legal patching (ambiguities closed per unit time), both measured in the same time unit. $G$ is a definition, not a dynamical model; it names the asymmetry without claiming to predict its trajectory. When $G > 1$, the stock $S$ of known-but-unpatched exploitable ambiguities grows: $dS/dt = R_d - R_p > 0$. The distinction between $G$ (the ratio) and $S$ (the stock) matters: $G$ can spike and then decay as the self-limiting dynamics in Section 4.4 operate, while $S$ continues to grow as long as $G$ remains above 1.

To make the definition operational, consider three heuristic regimes.

### 4.4 Illustrative dynamics

The regimes below are order-of-magnitude estimates, not measurements, and the per-regime rates are first converted to a common annual unit before the ratio is taken; treat the powers of ten as heuristic labels for the regime, not as a computed value of $G$. Three regimes correspond to three stages of AI adoption in legal-system exploitation.

**Pre-AI equilibrium ($G \approx 2$).** Both rates were measured in the same units: years of expert effort. A senior tax attorney or regulatory specialist identifies on the order of one exploitable ambiguity per year ($R_d \approx 1$/year). Congress patches roughly one major statutory gap per legislative session, about one every two years ($R_p \approx 0.5$/year). Courts resolve roughly one interpretive gap per circuit per five to ten years. Discovery was slow. Repair was slow. $S$ grew, but slowly enough that the system appeared stable.

**AI-assisted discovery, human execution ($G \approx 10^2$).** An RL agent parsing a regulatory corpus can flag on the order of one hundred candidate ambiguities per hour at near-zero marginal cost. Most of these are false positives, already-known items, or legally trivial findings. Conservative filtering, requiring that a flagged ambiguity be new, actionable, and non-obvious to a competent practitioner, reduces the raw output by roughly two orders of magnitude by way of illustration, leaving on the order of one actionable gap per week, or $R_d \approx 50$/year. The repair rate is unchanged from the pre-AI regime ($R_p \approx 0.5$/year): the same legislatures, the same courts, the same treaty bodies, operating at the same speed. $G \approx 100$. The stock of known-but-unpatched ambiguities grows linearly.

**AI-assisted discovery, agentic execution ($G \approx 10^3$+).** Discovery rate stays at the level above, but execution latency drops from months (human lawyers structuring transactions) to hours (autonomous agents filing documents, executing trades, submitting regulatory comments). The effective patch-gap widens because exploits are consumed faster than they can be closed. The stock of actively exploited ambiguities grows, not just the stock of known ones.

The point is structural, not the precision of the exponents: the numerator is moving to machine speed, the denominator is not, and the transition happens in stages with distinct governance signatures.

Three self-limiting dynamics prevent $G$ from growing without bound: (a) finite corpus, because the attack surface is large but bounded; (b) diminishing returns, because the easy loopholes are found first and each subsequent discovery requires more sophisticated search; and (c) legislative acceleration, because high-profile exploits trigger faster patching, as the Electoral Count Reform Act demonstrated. These limiters mean $G$ spikes during the initial AI-adoption phase and then decays toward some $G_\infty \geq 1$. But $S$, the stock of known-but-unpatched ambiguities, continues to grow as long as $G$ remains above 1. The open question is whether $G$ decays below 1 fast enough for $S$ to stabilize at a governable level. Adjacent formal systems already show the cost collapse; whether the legal penumbra follows at comparable speed is the unmeasured case.

### 4.5 Illustrative companion

A synthetic software companion generates $R_d$ from a budgeted, label-blind interface search on a HOT-designed rule graph; $G$ and the stocks $S_{\mathrm{known}}$ and $S_{\mathrm{active}}$ are outputs of that run, not inputs [33]. Cite the software concept DOI (always the latest zip). On that toy, three re-runnable checks hold: planted penumbra is recovered more often than under a same-size uniform-null labeling; the stock identity is obeyed while counted $R_d > R_p$; and sticky repair acceleration can drop $G$ while $S_{\mathrm{known}}$ is still rising.

Labeled figures live in the software record and are not reproduced here. Two of them earn a mention. One shows the $G$–$S$ split of Section 4.4 as a pair of stacked time series (no dual axis): after a salience-triggered rise in $R_p$, $G$ can fall while $S_{\mathrm{known}}$ is still increasing. Another compares searchers on the *same* HOT graphs: a neighborhood-spill rank recovers planted bridges; a degree-greedy rank recovers the dense core instead. The toy's penumbra result is therefore searcher-dependent. It does not show that statutes are HOT, and it does not show that an arbitrary optimizer will find Hart's penumbra.

The companion does not estimate legal $R_d$ or $R_p$, does not support the heuristic exponents above, and does not test whether any statute book is HOT.

## 5. Amplification Vectors

Three mechanisms scale the hackable-republic problem beyond what the pre-AI analyses anticipated.

### 5.1 Agentic autonomy: discovery vs. execution

Exploit discovery and exploit execution are distinct capabilities with different governance implications.

Discovery means an AI system identifies a regulatory gap and reports it to a human principal: "The portable-equipment exemption in Mississippi's air-quality registration process can be used for semi-permanent gas turbines if each unit is trailer-mounted." The governance problem here is a tool problem. Who controls access to the tool, and what disclosure obligations attach?

Execution means an AI agent files the documents, structures the transaction, and claims the exemption without human review. The governance problem here is an agency problem. Who bears liability when an autonomous agent acts on a discovered exploit?

As agentic deployment expands, the gap between discovery and execution shrinks. The Proskauer analysis [32] examines the legal consequences of AI agents committing to contracts without human review. The Gervais and Zhou results [10] show autonomous exploit execution in smart contracts at $0.01 per attempt. The legal system has no settled doctrine for AI agency.

The distinction matters for defense. Discovery can be governed by access controls and disclosure obligations. Execution requires agency law, liability assignment, and mandatory human-in-the-loop thresholds. Treating them as one problem guarantees that the policy response will be wrong for at least one of them.

### 5.2 Corpus scale

The Internal Revenue Code runs roughly 2,600 pages; the CCH annotated reporter, which practitioners actually search, approaches 70,000. The Code of Federal Regulations exceeds 180,000 pages. EU regulatory output is comparable. No human or team of humans has read all of it. Ruhl and Katz [22] show that this scale is itself measurable with the tools of complexity science, and that cross-references between statutes create interaction effects that no single drafter intended or foresaw.

An AI system can parse and cross-reference the entire corpus, identifying interactions that exist in the text but have never been noticed by any human reader. The attack surface is proportional to corpus size. AI is the first actor that can search the full surface.

### 5.3 Cross-jurisdictional arbitrage

Regulatory arbitrage predates AI by decades [16][17]. The 2015 JCPOA/UNSC maneuver was a case of routing around one jurisdiction's review process via another jurisdiction's authority [1]. The 2026 xAI data-center dispute in Southaven, Mississippi is a current example: state regulators classified up to 59 gas turbines as "temporary-mobile" units exempt from Clean Air Act permitting, a classification the NAACP, the Southern Environmental Law Center, and Earthjustice have challenged in federal litigation [27]. The permitting structure allowed the turbine expansion to sit on the Mississippi side of the Memphis airshed, where Mississippi's portable-equipment registration process is faster than Tennessee's federally delegated Title V program [28]. The U.S. EPA issued a January 2026 NSPS final rule (40 CFR 60 subpart KKKKa) creating a temporary-turbine subcategory, though its scope and enforceability remain contested between environmental groups and industry; the Department of Justice subsequently intervened, citing national security [29]. The case illustrates both the exploit (cross-jurisdictional classification arbitrage) and how quickly a high-visibility instance can draw a federal patch, consistent with the legislative-acceleration dynamic in Section 4.4.

AI accelerates the discovery of arbitrage opportunities across jurisdictions: regulatory sandboxes with weaker enforcement, conflicting definitions across state lines (the EU AI Act's fragmented national implementation is already producing this), and treaty obligations that override domestic law.

## 6. Defensive Measures and Their Structural Limits

### 6.1 Red-teaming the law

Liu et al. [9] propose using AI to stress-test proposed regulations before enactment: an autonomous loophole audit. This is the legal analogue of adversarial testing in software security.

The approach is promising but structurally bounded. Coverage is probabilistic, not exhaustive. The search space (all possible interpretations of a legal text under all possible future fact patterns) is unbounded. Red-teaming can reduce the stock of easily discoverable exploits. It cannot guarantee zero residual vulnerability. The same limitation applies to software fuzzing.

Red-teaming is effective against corporate optimizers, who exploit known patterns that automated testing can anticipate. It is less effective against misaligned autonomous agents, which discover unanticipated patterns by construction.

### 6.2 Formal methods for law

Computational law efforts [23] can shrink the attack surface by moving rule-system provisions from penumbra to core: translating ambiguous natural-language rules into decidable formal specifications. Section 4.2 gives the structural limit. Formalizing the penumbral provisions that constitute the primary attack surface destroys the adaptive capacity they were designed to preserve. Formal methods help at the margins. They cannot solve the problem.

### 6.3 Rate-limiting exploitation

In cybersecurity, when vulnerabilities cannot be eliminated, exploitation is rate-limited through access controls, monitoring, and disclosure requirements. Legal analogues exist and should be pursued:

Mandatory disclosure of AI use in regulatory filings and litigation. Several U.S. states and the EU AI Act already require this in specific contexts. Mandatory human-in-the-loop review for AI-assisted legal strategies above a consequence threshold, whether defined by dollar value, regulatory classification change, or cross-jurisdictional scope. Audit trails for AI-generated regulatory comments, detectable by agencies analyzing comment corpora.

These defenses do not close the patch-gap. They slow exploitation enough for human-speed patching to keep partial pace. They are the most immediately deployable measures and should be pursued regardless of their theoretical limitations.

### 6.4 The governance void

Any defensive framework is itself a rule system, and therefore itself subject to the same optimization dynamics it attempts to regulate. The EU AI Act defines "high-risk" AI systems using open-textured criteria ("significant risk to health, safety, or fundamental rights," Art. 6). An RL agent optimizing deployment strategy will treat those criteria as search space, just as it treats any other regulatory text.

The three results invoked below are theorems about computation and distributed systems, not about legal institutions. What follows is an analogical extension, not a formal derivation, and the analogy is stated explicitly rather than left implicit.

No general procedure can determine in advance whether an arbitrary program will satisfy a non-trivial semantic property, in the standard Turing-machine model of computation (Rice's theorem [30]; for application to autonomous governance, see [2]).

No deterministic protocol can guarantee agreement among distributed processes in an asynchronous network when even one process may crash (FLP impossibility, after Fischer, Lynch, and Paterson [31]; applied in [4]).

No feasible testing protocol can distinguish a compliant agent from a defecting one when the adversary selects the agent's behavior after the verifier commits (attestation bounds from cryptographic complexity; formalized in [3]).

Each rests on a different branch of mathematics, and each assumes a formal model, computability, asynchronous message-passing, or a computationally bounded adversary, that a legal system does not literally instantiate. The claim is not that courts are Turing machines or that legislatures are asynchronous consensus protocols. The claim is that the same qualitative obstruction recurs: a system that must decide, in finite time and under some information constraint, whether an agent will comply with an open-ended specification runs into a version of the same wall each of these theorems describes in its own domain. Defeating any one obstruction does not resolve the other two. Together they motivate, without formally proving, why the governance void resists closure by governance engineering alone.

The military case and the civilian case are two manifestations of the same underlying tension. The sovereign position becomes harder to occupy when the rate of exception-generation exceeds the rate of sovereign ratification, whether the rate is set by physics (latency) or by optimization (reward hacking).

## 7. Predictions

Three falsifiable predictions bound the paper's empirical commitments.

**Prediction 1: AI-generated regulatory comments at detectable scale.** By end of 2027, at least one U.S. federal rulemaking proceeding will have a detectable, non-trivial fraction of its substantive comments generated by AI systems on behalf of commenting parties (as distinct from agencies' own use of AI to process received comments, which is already underway). These will be individually reasoned legal arguments identifying specific ambiguities in the proposed rule, not form letters. Documentation will come from the agency, from researchers analyzing the comment corpus, or from investigative journalism.

**Prediction 2: AI-discovered legal exploit in production.** By end of 2027, at least one documented case will show a firm using an AI system to identify and act on a regulatory gap, where the firm or an enforcement agency attributes the gap-finding to an AI system in an enforcement record, 8-K filing, or official report.

**Prediction 3: Defensive deployment.** By mid-2028, at least two national governments or the EU will deploy AI systems to red-team draft legislation before enactment, producing public reports on discovered ambiguities.

## 8. Conclusion

The hackable republic is not a loose metaphor. It is a structural property of rule systems, identified in political philosophy from Joly to Schmitt, described technically by Hart as open texture, documented in the regulatory-arbitrage literature, and now scaling with AI capabilities.

The governance patch-gap, the asymmetry between machine-speed exploit discovery and human-speed legal repair, is a central AI governance problem that existing frameworks do not fully address, because they are themselves rule systems subject to the same optimization dynamics. The EU AI Act, U.S. executive orders on AI, and voluntary industry commitments are all specifications written in natural language with open-textured provisions. Each is a new attack surface.

The argument has three load-bearing weaknesses worth naming plainly. The structural isomorphism between reward functions and regulatory frameworks (Section 3.4) is asserted and illustrated, not independently tested against a case where it fails to hold; a counterexample would weaken the paper's central claim more than any of the four evidence lines individually. The regime estimates in Section 4.4 are order-of-magnitude heuristics built on sparse and partly anecdotal rate data, not measurements, and should be read as illustrating a direction rather than quantifying it. And the strongest single piece of direct evidence for AI-driven societal hacking, the SocioHack experiment (Section 3.4), remains an unreplicated preprint; the paper's conclusions are constructed to survive its failure to replicate, but they would be better supported if it does.

The question is not whether AI will be used to exploit legal systems; Section 3.4's second, third, and fourth evidence lines, independent of SocioHack, already show AI-accelerated exploit discovery in adjacent formal and quasi-formal rule systems. The open question is whether the patch cycle can be accelerated enough to keep the stock of exploitable ambiguities within bounds. Adjacent formal systems already show the cost collapse; whether the legal penumbra follows at comparable speed is the unmeasured case.

## AI Utilization Statement

This work was produced with AI assistance . The author used Claude Opus 4.6 for drafting and structural editing, and Kimi 2.6 and Grok 4.6 for GAN-like adversarial reviews. All substantive claims, analytical decisions, structural choices, and final editorial judgments were made by the author. AI-generated content was reviewed and corrected by the author before inclusion. 

## References

[1] D. Y. Bilar, "Republics as hackable systems," Medium, Jul. 2015. [Online]. Available: https://medium.com/@daniel_bilar/republics-as-hackable-systems-e7b659143b0

[2] D. Y. Bilar, "On the Necessary Void at the Center of Autonomous Governance," Zenodo, 2026. doi: 10.5281/zenodo.20190801. [Online]. Available: https://zenodo.org/records/20190801

[3] D. Y. Bilar, "Three Regimes of Capability Attestation for Autonomous Agents," Zenodo, 2026. doi: 10.5281/zenodo.20114610. [Online]. Available: https://zenodo.org/records/20114610

[4] D. Y. Bilar, "Golden Dome Latency Governance: Autonomous Operations Model Extended to Boost-Phase Intercept Timelines," Zenodo, 2026. doi: 10.5281/zenodo.19368682. [Online]. Available: https://zenodo.org/records/19368682

[5] D. Y. Bilar, "The Decision Nobody Makes: America's Autonomous Weapons Have a Sovereignty Problem That Can't Be Fixed," Medium, May 2026. [Online]. Available: https://medium.com/@daniel_bilar/the-decision-nobody-makes-941de22783ff

[6] H.L.A. Hart, *The Concept of Law*, Oxford: Clarendon Press, 1961. [Online]. Available: https://global.oup.com/academic/product/the-concept-of-law-9780198761235

[7] C. Schmitt, "Political Theology: Four Chapters on the Concept of Sovereignty," G. Schwab (trans.), Chicago: University of Chicago Press, 1922/2005. [Online]. Available: https://press.uchicago.edu/ucp/books/book/chicago/P/bo3641063.html

[8] M. Joly, *Dialogue aux Enfers entre Machiavel et Montesquieu*, Brussels, 1864. [Online]. Available: https://gallica.bnf.fr/ark:/12148/bpt6k742943.texteImage

[9] W. Liu, X. Mou, H. Yan, Z. Wei, Y. He, "Large Language Models Hack Rewards, and Society," arXiv:2606.04075, Jun. 2026. [Online]. Available: https://arxiv.org/abs/2606.04075

[10] A. Gervais, L. Zhou, "AI Agent Smart Contract Exploit Generation," arXiv:2507.05558, Jul. 2025. [Online]. Available: https://arxiv.org/abs/2507.05558

[11] J. M. Carlson and J. Doyle, "Complexity and robustness," *PNAS*, vol. 99, suppl. 1, pp. 2538-2545, 2002. doi: 10.1073/pnas.012582499. [Online]. Available: https://www.pnas.org/doi/10.1073/pnas.012582499

[12] B. Schneier, *A Hacker's Mind: How the Powerful Bend Society's Rules, and How to Bend Them Back*, New York: W.W. Norton, 2023. [Online]. Available: https://www.schneier.com/books/a-hackers-mind/

[13] R. Calo, "Robotics and the Lessons of Cyberlaw," *California Law Review*, vol. 103, no. 3, pp. 513-563, 2015. doi: 10.2139/ssrn.2402972. [Online]. Available: https://ssrn.com/abstract=2402972

[14] K. L. Scheppele, "Autocratic Legalism," *University of Chicago Law Review*, vol. 85, no. 2, pp. 545-583, 2018. [Online]. Available: https://chicagounbound.uchicago.edu/uclrev/vol85/iss2/2

[15] S. Levitsky and D. Ziblatt, *How Democracies Die*, New York: Crown, 2018. [Online]. Available: https://www.penguinrandomhouse.com/books/552516/how-democracies-die-by-steven-levitsky-and-daniel-ziblatt/

[16] R. Romano, "The Advantage of Competitive Federalism for Securities Regulation," AEI Press, 2002. [Online]. Available: https://www.aei.org/research-products/book/the-advantage-of-competitive-federalism-for-securities-regulation/

[17] V. Fleischer, "Regulatory Arbitrage," *Texas Law Review*, vol. 89, pp. 227-289, 2010. [Online]. Available: https://ssrn.com/abstract=1567212

[18] D. Amodei et al., "Concrete Problems in AI Safety," arXiv:1606.06565, Jun. 2016. [Online]. Available: https://arxiv.org/abs/1606.06565

[19] J. Skalse, N. Howe, D. Krasheninnikov, D. Krueger, "Defining and Characterizing Reward Gaming," *NeurIPS*, vol. 35, pp. 9460-9471, 2022. [Online]. Available: https://proceedings.neurips.cc/paper_files/paper/2022/hash/3d719fee332caa23d5038b8a90e81796-Abstract-Conference.html

[20] D. Manheim and S. Garrabrant, "Categorizing Variants of Goodhart's Law," arXiv:1803.04585, 2018. [Online]. Available: https://arxiv.org/abs/1803.04585

[21] V. Krakovna et al., "Specification gaming examples in AI: master list," ongoing catalog. [Online]. Available: https://docs.google.com/spreadsheets/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml ; accompanying discussion at https://vkrakovna.wordpress.com/2018/04/02/specification-gaming-examples-in-ai/

[22] J. B. Ruhl and D. M. Katz, "Measuring, Monitoring, and Managing Legal Complexity," *Iowa Law Review*, vol. 101, pp. 191-244, 2015. [Online]. Available: https://ssrn.com/abstract=2566535

[23] D. Merigoux, N. Chataing, J. Protzenko, "Catala: A Programming Language for the Law," *Proc. ACM Program. Lang.* (ICFP), vol. 5, no. ICFP, article 77, pp. 1-29, 2021. doi: 10.1145/3473582. [Online]. Available: https://dl.acm.org/doi/10.1145/3473582

[24] Electoral Count Reform and Presidential Transition Improvement Act of 2022, Pub. L. 117-328, Div. P, 136 Stat. 5233. [Online]. Available: https://www.congress.gov/bill/117th-congress/senate-bill/4573

[25] D. Citron and F. Pasquale, "The Scored Society: Due Process for Automated Predictions," *Washington Law Review*, vol. 89, pp. 1-33, 2014. [Online]. Available: https://ssrn.com/abstract=2376209

[26] J. Balkin, "The Path of Robotics Law," *California Law Review Circuit*, vol. 6, pp. 45-60, 2015. [Online]. Available: https://www.californialawreview.org/online/the-path-of-robotics-law

[27] Mississippi Today, "State sets dates to retire temporary xAI turbines," Jul. 2026. [Online]. Available: https://mississippitoday.org/2026/07/31/southaven-xai-turbines-deadline/

[28] Mississippi Today, "xAI now has 46 gas turbines without air permits," May 2026. [Online]. Available: https://mississippitoday.org/2026/05/11/xai-46-gas-turbines-no-air-permits/

[29] Turbomachinery Magazine, "DOJ Intervenes in xAI Gas Turbine Lawsuit, Citing National Security," Jun. 2026. [Online]. Available: https://www.turbomachinerymag.com/view/doj-intervenes-in-xai-gas-turbine-lawsuit-citing-national-security

[30] H. G. Rice, "Classes of Recursively Enumerable Sets and Their Decision Problems," *Transactions of the American Mathematical Society*, vol. 74, no. 2, pp. 358-366, 1953. doi: 10.1090/S0002-9947-1953-0053041-6.

[31] M. J. Fischer, N. A. Lynch, M. S. Paterson, "Impossibility of Distributed Consensus with One Faulty Process," *Journal of the ACM*, vol. 32, no. 2, pp. 374-382, 1985. doi: 10.1145/3149.214121.

[32] P. J. Cramer, J. Mollod, C. E. Rimmer, "Contract Law in the Age of Agentic AI: Who's Really Clicking 'Accept'?," Proskauer Rose LLP, New Media and Technology Law Blog, Apr. 2025. [Online]. Available: https://www.proskauer.com/blog/contract-law-in-the-age-of-agentic-ai-whos-really-clicking-accept

[33] D. Y. Bilar, "patch-gap-hot-search: a synthetic HOT-searcher toy for the governance patch-gap," Zenodo, 2026. doi: 10.5281/zenodo.21918091. [Online]. Available: https://doi.org/10.5281/zenodo.21918091
