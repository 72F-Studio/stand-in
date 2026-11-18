# Evidence: where to look, how to log it, how to rate it

## Contents

- Source types
- Search patterns
- The evidence log
- Confidence rubric
- Known biases to state

## Source types

Ordered roughly from strongest to weakest for predicting what people do.

| Type | Examples | Good for | Watch for |
| --- | --- | --- | --- |
| Behavioural data | Official statistics, usage and market-share figures, published churn or adoption numbers, time-use surveys | What people actually do, how many | Often coarse; rarely segment-specific |
| Representative surveys | Pew, national statistics offices, large industry surveys with a stated method | Prevalence of attitudes across demographics | Stated, not observed; check sample and date |
| Academic and practitioner studies | Peer-reviewed papers, published usability studies, public research repositories | Mechanisms, why people behave as they do | Small or student samples; different context |
| Reviews | App stores, G2, Capterra, Trustpilot, Amazon, Product Hunt | Concrete pains and delights with existing products | Extremes over-represented; fake reviews |
| Community discussion | Reddit, Hacker News, Stack Exchange, niche forums, Discord or Facebook groups with public pages, YouTube comments | Language people use, workarounds, context | Vocal minority; community-specific culture |
| Social posts | X, LinkedIn, TikTok, Mastodon, Bluesky | Fresh reactions, emerging complaints | Performative; algorithmic amplification |
| Vendor content | Competitor blogs, case studies, marketing surveys | What competitors believe sells | Self-interested; treat claims as claims |

Prefer several source types over many sources of one type. Ten threads from
the same subreddit are one source for the purpose of independence.

## Search patterns

Search in the audience's words, not the product's. Useful shapes:

- Pain: `"<task>" frustrating`, `"I hate" <task>`, `<task> "takes forever"`
- Workarounds: `"how do you" <task>`, `"I just use" <tool> for <task>`,
  `<task> spreadsheet template`
- Switching: `"switched from" <competitor>`, `"cancelled" <competitor> why`,
  `<competitor> alternative`
- Spending: `"worth paying for" <category>`, `<competitor> pricing "too expensive"`
- Indifference: `"do I really need" <category>`, `<category> overrated`
- Segment-scoped: add `site:reddit.com/r/<community>`, a profession, a life
  stage, or a region to any of the above
- Numbers: `<audience> survey <year>`, `<category> usage statistics`,
  `<audience> time use`

Run the disconfirming searches (switching, indifference) every time, not
only when the first results look too rosy.

Open the pages that matter instead of relying on snippets. Note the date:
anything older than about three years is background unless the behaviour is
slow-changing.

## The evidence log

Keep one numbered list for the session. Each entry:

```
[n] Source: <site and page title>
    URL: <link to the page or thread>
    Date: <published or posted; "undated" if unknown>
    Type: <row from the source types table>
    Who is speaking: <segment, as far as the page shows>
    Signal: <one or two sentences, paraphrased; a short verbatim quote only
            if it is not personally revealing>
    Scale: <one post / thread with ~N agreeing replies / survey of N / etc.>
    Retrieved: <opened in full | search snippet only | supplied by user>
```

Record who is speaking with care. A complaint from an enterprise admin is
not evidence about a hobbyist. If the page does not reveal the segment,
write "unknown" and let that lower confidence.

## Confidence rubric

Rate the claim for the persona's segment, not the topic in general.

| Level | Requires |
| --- | --- |
| **High** | Three or more independent sources of at least two types, including behavioural or representative data; recent; speakers clearly match the segment; no substantial contradicting evidence |
| **Medium** | Two or more independent sources that agree, with a reasonable segment match; or one strong representative source. Prevalence may be unknown |
| **Low** | A single source, an anecdotal thread, a loose segment match, dated material, conflicting evidence, or inference from adjacent behaviour |
| **No data** | Nothing retrieved bears on the question. Say so; do not answer in character |

Caps that override the table:

- Predictions of future behaviour toward a product that does not exist
  (would use, would pay, would switch): **Low** at most.
- Model knowledge with no retrieved source: **Low**, labelled
  `Unverified (model prior)`.
- Search-snippet-only evidence: **Medium** at most.
- Vendor-authored evidence alone: **Low**.
- All sources from one community or one platform: **Medium** at most.
- Extrapolating to a demographic the sources do not show (another country,
  age group, income level): drop one level and say that you extrapolated.

The reasoning sentence should name the weakest link, for example: "Medium.
Three threads agree, but all are from one subreddit of power users."

## Known biases to state

Mention the ones that apply when they affect a conclusion:

- **Vocal sampling**: people who post are unusual. Satisfied and indifferent
  people are nearly invisible online.
- **Negativity and extremity**: reviews cluster at one and five stars.
- **Survivorship**: forums for a tool contain people who still use it.
- **Platform demographics**: each platform skews by age, gender, region,
  profession and language. English-language sources say little about other
  markets.
- **Astroturfing and incentives**: paid reviews, affiliate posts, vendor
  employees in threads.
- **Recency drift**: attitudes toward fast-moving categories date quickly.
- **Say versus do**: stated preferences routinely differ from behaviour.
- **Model bias**: the role-play itself tends toward agreeable, articulate,
  averaged answers. Real people are less coherent and more surprising.
