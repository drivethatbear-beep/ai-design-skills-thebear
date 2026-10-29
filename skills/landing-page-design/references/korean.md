# Korean locale (한국어 페이지)

Read when the page copy is Korean. Each rule below overrides the matching rule in SKILL.md. Everything not mentioned here still applies as written.

---

## K1. Fonts

**Default: Pretendard.** It covers Hangul, Latin, and numerals in one family, so the one typeface rule from B1 holds without pairing.

```html
<link rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
```

```css
font-family: "Pretendard Variable", Pretendard, -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
```

System fallbacks after the primary face are fine. The checker only judges the first family in a stack.

**Alternatives, only on request:** SUIT, Wanted Sans.

**Never as the primary face:** Noto Sans KR, Nanum Gothic, Malgun Gothic (맑은 고딕), Gulim, Dotum, Batang. They read as an unconsidered default, the Korean equivalent of Inter and Arial.

**Weights.** Headings 600 to 700, body 400, labels 500. The B1 cap still holds: nothing above 700.

**No oblique.** Hangul has no italic. Never let the browser synthesize one, which means no `font-style: italic` on Korean text and `font-synthesis: none` on the root.

**Numbers.** Use `font-variant-numeric: tabular-nums` on prices, stats, and tables so digits line up.

## K2. Line breaking

Korean breaks between syllables by default, which splits words in half. Set this on the root:

```css
html { word-break: keep-all; overflow-wrap: break-word; line-break: strict; }
```

Tailwind: `break-keep` on the body, plus `[overflow-wrap:break-word]` only if long URLs appear.

- **Orphans.** The B1 orphan rule applies to 어절. One 어절 alone on the last line is an orphan. `keep-all` plus `text-wrap: balance` on headings handles most cases. Check at 360px, 768px, and 1280px.
- **Hero line breaks.** Break between 의미 단위, never between a modifier and the noun it modifies. When a break that works on desktop hurts mobile, scope it: `<br class="hidden md:inline">`.

## K3. Type scale adjustments

Hangul fills the em box more than Latin, so the same size reads larger and denser.

| Use | Size step | Line height | Tracking |
|---|---|---|---|
| Hero heading | `text-5xl` to `text-6xl` | `leading-tight` (1.25) | `tracking-tight` |
| Section heading | `text-3xl` to `text-4xl` | `leading-snug` (1.375) | `tracking-tight` |
| Body | `text-base` to `text-lg` | `leading-relaxed` (1.625) | `tracking-normal` |
| Caption, label | `text-sm` | the step's own | `tracking-normal` |

This table is the one sanctioned exception to "line height comes from the step" in B1. Steps `text-5xl` and above ship with a line height of 1, which clips two line Korean headlines. Never use positive tracking on Korean text, and never set body copy below `text-base`.

## K4. Copy rules (한국어 카피)

**Register.** 존댓말 throughout. 합니다체 for B2B and professional offers, 해요체 for consumer products. Pick one per page and never mix them.

**CTA.** A concrete action plus what the visitor gets, ending in a verb: "무료로 시작하기", "상담 예약하기", "체크리스트 받기". Never "자세히 보기", "더 알아보기", "확인", or "제출" as the primary CTA.

**Headline formulas** (from A5, in Korean):
- "{고통} 없이 {결과}"
- "{대상}을 위한 {카테고리}"
- "{기간} 만에 {결과}"

**Banned filler.** 혁신적인, 획기적인, 차원이 다른, 압도적인, 새로운 패러다임, 원스톱, 토탈 솔루션, 극대화, 스마트한, 퀄리티 높은. Say what the product does instead.

**Superlatives need proof.** 최고, 최초, 유일, 1위, and 국내 최대 need objective evidence under the 표시·광고의 공정화에 관한 법률. Either cite the source and its 기준일 next to the claim, or drop the claim.

**Punctuation.** The B1 hyphen ban applies. A tilde is allowed only for numeric ranges ("3~5일"). No exclamation marks, no emoji in system messages.

**Numbers.** Pick one money format per page: "49,000원" or "4만 9천 원". Pick one date format: "2026년 10월 29일" or "2026.10.29.". B8 realism still applies, so avoid round numbers.

**People and companies.** Full Korean names (성 + 이름), with surnames varied beyond 김, 이, 박. Invented company names should fit the industry: "한빛정밀", "새솔물류", not generic tech startup names. Never use a real company's name or logo as a customer without permission.

**System messages.** Calm and specific, in the page's register:
- "견적서를 김다은 님께 보냈어요."
- "업로드하지 못했어요. 파일이 20MB를 넘습니다."

## K5. Korea ship requirements

These extend B10. Cookie consent banners are generally not required in Korea; add one only for EU traffic or on request.

**Footer**
- **개인정보처리방침** link, set bolder than the other footer links so visitors can find it easily.
- 이용약관 link.
- 사업자 정보: 상호, 대표자, 주소, 사업자등록번호, 연락처, 이메일.
- If the site sells online, also 통신판매업 신고번호 and a 사업자정보 확인 link, per the 전자상거래법.

**Forms that collect personal data**
- A 개인정보 수집·이용 동의 checkbox that states the 수집 항목, 목적, 보유·이용 기간, and the right to refuse along with what refusing means (개인정보 보호법 제15조).
- Unchecked by default.
- Marketing 수신 동의 is a separate, optional checkbox, never bundled with the required one (정보통신망법 제50조).

**Meta and sharing**
- `<html lang="ko">` and `og:locale` set to `ko_KR`.
- `og:image` at 1200×630 renders on KakaoTalk, Naver, and Facebook.
- For indexed pages, register with Naver Search Advisor and add its `naver-site-verification` meta tag.

**Contact**
- On mobile, phone numbers are `tel:` links.
- A KakaoTalk 채널 link is a secondary contact. It never competes with the primary CTA above the fold.

---

## Checklist

- [ ] Pretendard as the primary face, no oblique, `font-synthesis: none`
- [ ] `word-break: keep-all` on the root; no orphaned 어절 at 360, 768, 1280px
- [ ] Headline line height per K3; body at least `text-base` with `leading-relaxed`
- [ ] One register; CTA ends in a concrete verb; no banned filler; superlatives cited
- [ ] Footer: 개인정보처리방침 (bold), 이용약관, 사업자 정보
- [ ] Consent checkbox with all four disclosures, unchecked; marketing consent separate
- [ ] `lang="ko"`, `og:locale`, and a 1200×630 og:image
