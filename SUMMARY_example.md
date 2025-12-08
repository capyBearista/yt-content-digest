### Video Content Summary
The creator gives a first‑hand impression of **Zed**, a Rust‑based IDE positioned as a high‑performance alternative to tools like VS Code, Cursor, and Antigravity. After years with Emacs and a brief stint on Cursor, he evaluates Zed’s interface, speed, AI‑assisted coding, and extensibility. He notes the astonishing 120 fps tab switching demo, instantaneous editor response, and the “agent communication protocol” (ACP) that lets users plug in external code‑generation agents (e.g., Cloud Code, Cerebras, Open Code). Vim motions are supported by default, a Helix‑style mode is included, and extensions install almost instantly. The video also covers Zed Pro’s subscription model, the built‑in “collab” feature for real‑time pair programming, and the background of the founders (including former Atom developer Nathan Sobo). Throughout, the presenter balances praise for performance and openness with criticism of missing debugger support, limited UTF‑8‑only file handling, and a pricing structure that may not suit everyone. The tone remains skeptical yet appreciative, concluding that Zed is worth trying, especially for users craving speed and an open‑source footprint.

### Key Insights
- **Performance & UI Smoothness** (Time: 01:10) – The creator claims Zed’s tab switching runs at 120 fps, making the editor feel “instantaneous” compared to VS Code or Cursor.  
- **AI & ACP Integration** (Time: 03:30) – Zed ships with an “agent communication protocol” allowing built‑in or external AI agents (Cloud Code, Cerebras, Open Code) and can be toggled off via a master switch.  
- **Vim & Helix Modes** (Time: 02:30) – Vim motions work out‑of‑the‑box and a Helix‑style mode is also provided, satisfying users who prefer modal editing.  
- **Extension Installation Speed** (Time: 01:55) – Extensions install “comically fast,” a feature the creator highlights despite it not being a typical purchasing decision factor.  
- **Collaboration (Collabs) Feature** (Time: 06:20) – Real‑time shared editing with voice‑chat channels is possible, and the creator notes a Hacker News article praising this workflow.  
- **Pricing & Zed Pro** (Time: 05:45) – Zed Pro costs $10 /mo, bundles Frontier models and raises token limits, but the creator questions its value given a 10 % premium over the free tier.  
- **Missing Debugger & UTF‑8 Limitation** (Time: 07:50) – The video acknowledges the absence of a built‑in debugger and the restriction to UTF‑8 files only, which some users find limiting.

### Detailed Breakdown
| Feature | Verdict |
|---------|---------|
| **Performance (120 fps UI)** | Strong – perceived as markedly faster than VS Code/Cursor. |
| **AI Predictions (ACP, built‑in agents)** | Good – flexible choice of agents; master switch to disable. |
| **Vim/Helix Modes** | Positive – solid support for modal editing out‑of‑the‑box. |
| **Extension Install Speed** | Excellent – near‑instant installation. |
| **Collaboration (Collabs)** | Powerful – real‑time shared editing with voice channels. |
| **Zed Pro Pricing** | Mixed – added features but 10 % premium may deter some users. |
| **Debugger Support** | Lacking – no native debugger, noted as a pain point. |
| **File Format Support** | Restrictive – only UTF‑8 files accepted. |
| **Theme & UI Customization** | Limited – few built‑in themes; extensions needed for more. |
| **Community Extensibility (Rust UI lib)** | Promising – open‑source UI library could enable plugins later. |

### Community Intelligence
**Overall**: Predominantly **Positive** (≈ 65 % of high‑like comments praise speed, AI, and Vim mode) with a **Mixed** undercurrent of criticisms about missing debugger, UTF‑8 restriction, and pricing.

**Positive Highlights**  
- *Speed & Efficiency*: “ultra fast and efficient, it almost eats no ram” – @codeking4585 (206 likes).  
- *AI Disable Switch*: “The best feature … disable AI out of the box.” – @smrenatox (103 likes).  
- *Vim/Helix Appeal*: “Love Zed … simple, uncomplicated, uncluttered” – @benheidemann3836 (101 likes).  

**Criticisms/Negatives**  
- *Missing Debugger*: “The Rust debugging is difficult to set up in Zed.” – @branislav3800 (1 like).  
- *UTF‑8 Only*: “Zed refuses to open any files other than proper UTF‑8 encoded text files.” – @ghuxi (7 likes).  
- *Pricing Concerns*: “They’re charging a +10 % premium to people who are already paying pro.” – @stefankyriacou7151 (3 likes).  

**Community Knowledge (Corrections, Disputes, & Tips)**
- **Additive Tip**: @theintjengineer suggests using external agents (Cloud Code, Open Code) for smoother AI interaction.  
- **Correction**: @ldov6373 reports that on Windows the editor did not feel faster than VS Code, noting monitor refresh rate may affect perceived performance.  
- **Additive Tip**: @lampjustin points out the newly added Helix bindings (02:46) as a reason to revisit Zed.  
- **Correction**: @niaa (anonymous) highlights that Zed’s built‑in AI predictions are sourced from Zed by default but can be swapped for Copilot or Code Straw, clarifying the source switch.  
- **Additive Tip**: @swordofthemorning777 mentions that because Zed is open‑source, users can contribute fixes or request features directly in Rust.  

---

==============================
RAW DATA
==============================
TITLE: Zed the IDE (Yes, I tried Cursor & Antigravity)
DESCRIPTION:
My first impressions of Zed after a spending a few years using Emacs and a short stint with Cursor.

Thanks to Zed for sponsoring! https://zed.dev/

Keyboard: Glove80 - https://bit.ly/3EKyn7X
Camera: Canon EOS R8 https://amzn.to/4gSpivt
Monitor: Dell U4914DW 49in https://amzn.to/3MJV1jx
Microphone: Sennheiser 416 https://amzn.to/3Fkti60
Microphone Interface: Focusrite Clarett+ 2Pre https://amzn.to/3J5dy7S
Tripod: JOBY GorillaPod 5K https://amzn.to/3JaPxMA
Mouse: Razer DeathAdder https://amzn.to/3J9fYCf
Computer: 2021 Macbook Pro https://amzn.to/3J7FXtW
Lens: Canon RF50mm F 1.2L USM https://amzn.to/3qeJrX6
Caffeine: High Brew Cold Brew Coffee https://amzn.to/3hXyx0q
More Caffeine: Monster Energy Juice, Pipeline Punch https://amzn.to/3Czmfox
Building A Second Brain book: https://amzn.to/3cIShWf

TRANSCRIPT:
[2.000s -> 4.000s] Zed has an interesting place in this whole scene. I thought it would be kind
[4.000s -> 6.000s] of like cursor but snappier and less
[6.000s -> 8.000s] resource hungry. That assumption was
[8.000s -> 11.000s] dead wrong. This is my journey so far. I
[11.000s -> 13.000s] still love Emacs. It's just not a
[13.000s -> 16.000s] perfect fit for me anymore. Cursor was
[16.000s -> 18.000s] the clear AI leader, but others have
[18.000s -> 20.000s] caught up. And anti-gravity is
[20.000s -> 22.000s] promising, but it's not quite there yet.
[22.000s -> 24.000s] I've been curious about Zed for a while,
[24.000s -> 27.000s] so here we are. I use Vim Motions 99% of
[27.000s -> 29.000s] the time. I currently have a slight
[29.000s -> 30.000s] preference for terminal editors, but
[30.000s -> 33.000s] that's not strict. I value agentic
[33.000s -> 35.000s] coding features. I was surprised at how
[35.000s -> 37.000s] different Zed's approach to agentic
[37.000s -> 38.000s] coding is from something like cursor.
[38.000s -> 40.000s] We'll get to that. And the story of the
[40.000s -> 43.000s] people behind Zed and how it came about.
[43.000s -> 44.000s] You can't make this stuff up. We'll get
[44.000s -> 46.000s] to that, too. This video is sponsored by
[46.000s -> 48.000s] Zed, but if you think that's going to
[48.000s -> 50.000s] influence my opinions, just wait.
[50.000s -> 52.000s] Anyway, let's get into it. At first
[52.000s -> 54.000s] glance, the interface looks pretty
[54.000s -> 56.000s] unremarkable. Great start to a sponsored
[56.000s -> 58.000s] video. I know this feature is the
[58.000s -> 60.000s] cornerstone of Zed's marketing strategy.
[60.000s -> 62.000s] Ready for it? Are you ready? Boom. There
[62.000s -> 64.000s] it is. I'm not even kidding. This is the
[64.000s -> 65.000s] very first thing they show in the demo
[65.000s -> 68.000s] video on their website. Jokes aside, it
[68.000s -> 70.000s] actually is an impressive demo. In the
[70.000s -> 71.000s] video, the tab switching is actually
[71.000s -> 74.000s] happening at 120 frames per second. So,
[74.000s -> 76.000s] the gamers are going to be very jealous.
[76.000s -> 78.000s] Seriously though, working in the editor
[78.000s -> 81.000s] feels instantaneous. It feels
[81.000s -> 82.000s] considerably different than something
[82.000s -> 84.000s] like a VS Code or cursor. But yeah, the
[84.000s -> 87.000s] first core tenant of Zed's vision is a
[87.000s -> 89.000s] dedication to optimal performance. As
[89.000s -> 91.000s] they say, even subperceptual pauses add
[91.000s -> 93.000s] up over the course of a day to create
[93.000s -> 95.000s] unnecessary stress. Probably true, but
[95.000s -> 96.000s] the irony here is that the founder of
[96.000s -> 98.000s] Zed may have a connection to the slower
[98.000s -> 100.000s] performance of VS Code and Cursor. We'll
[100.000s -> 102.000s] get to that. One of Zed's claims to fame
[102.000s -> 104.000s] is that it's written in Rust. Some might
[104.000s -> 106.000s] use it just because of that, but in
[106.000s -> 108.000s] addition to speed and memory efficiency,
[108.000s -> 110.000s] that theoretically should help with
[110.000s -> 113.000s] stability, too. Let's talk about themes.
[113.000s -> 115.000s] Out of the box, we have Grubbox, AU, One
[115.000s -> 117.000s] Dark. They do have the retina destroying
[117.000s -> 119.000s] light variants in there, too, if you're
[119.000s -> 121.000s] into that. Why? Why would you? You can
[121.000s -> 122.000s] get more themes via extensions if you
[122.000s -> 125.000s] like. It's actually comical how fast
[125.000s -> 127.000s] extensions install. Nobody picks an IDE
[127.000s -> 129.000s] for extension installation speed, but
[129.000s -> 132.000s] but still. AI edit predictions seem
[132.000s -> 133.000s] pretty good, roughly in line with what
[133.000s -> 135.000s] you get with Copilot or Incursor. Press
[135.000s -> 137.000s] tab if you like what it gives you, or
[137.000s -> 139.000s] just ignore them. By default, these
[139.000s -> 141.000s] predictions are sourced from Zed, but
[141.000s -> 143.000s] you have the option to source them from
[143.000s -> 146.000s] Copilot or Code Straw instead. Zed does
[146.000s -> 147.000s] have a Vim mode. For me, that's a strict
[147.000s -> 149.000s] requirement. If you're using Vid Mode,
[149.000s -> 151.000s] you probably want relative line numbers.
[151.000s -> 153.000s] We have that. They even have a helix
[153.000s -> 155.000s] mode. I did not expect that. There is an
[155.000s -> 158.000s] AI master switch, so you can completely
[158.000s -> 160.000s] turn off AI. John Connor's with me on
[160.000s -> 161.000s] that. With regards to moving around in
[161.000s -> 163.000s] the editor, you can set it up so the
[163.000s -> 165.000s] common VS Code and cursor commands work.
[165.000s -> 167.000s] Like command shift P to bring up the
[167.000s -> 169.000s] command pallet, command option O to
[169.000s -> 171.000s] search symbols in the buffer, command P
[171.000s -> 173.000s] to bring up telescope. I mean the fuzzy
[173.000s -> 175.000s] file picker. Vim motions in editors that
[175.000s -> 177.000s] aren't Vim are always interesting
[177.000s -> 179.000s] because the basics are usually there,
[179.000s -> 181.000s] but they can't possibly have every
[181.000s -> 183.000s] binding from every plugin that you use.
[183.000s -> 185.000s] I was pleasantly surprised to find that
[185.000s -> 187.000s] Vim surround motions work. I suspect
[187.000s -> 189.000s] that's one most people want. What I
[189.000s -> 190.000s] couldn't find right away was something
[190.000s -> 193.000s] like flash.invim or Helix's go-to word
[193.000s -> 195.000s] function, which makes you feel like
[195.000s -> 196.000s] you're controlling the editor
[196.000s -> 198.000s] telekinetically. There's a discussion
[198.000s -> 200.000s] about this on GitHub, so I know I'm not
[200.000s -> 202.000s] the only one. Okay, AI coding. First of
[202.000s -> 205.000s] all, like I said, there is a disable AI
[205.000s -> 206.000s] master switch that some people will
[206.000s -> 208.000s] appreciate, but Skynet said I had to
[208.000s -> 210.000s] leave it on for the rest of this video.
[210.000s -> 212.000s] Zed introduced this thing called ACP or
[212.000s -> 215.000s] agent communication protocol and it aims
[215.000s -> 217.000s] to standardize how ids communicate with
[217.000s -> 219.000s] external coding agents. Examples being
[219.000s -> 222.000s] cloud code, open code and so on. It
[222.000s -> 224.000s] seems wellreceived by the industry
[224.000s -> 225.000s] because it's already in a lot of
[225.000s -> 228.000s] mainstream IDEs and agents. From a user
[228.000s -> 230.000s] perspective, ACP is really under the
[230.000s -> 231.000s] hood. You're still just interacting with
[231.000s -> 233.000s] zed output and file diff show right in
[233.000s -> 236.000s] the editor just like you'd expect. But
[236.000s -> 238.000s] it's nice because if you already have a
[238.000s -> 239.000s] subscription with one of the agent
[239.000s -> 241.000s] providers I mentioned, you can just
[241.000s -> 243.000s] continue to use that subscription. Here
[243.000s -> 245.000s] I'm using Cloud Code with my existing
[245.000s -> 247.000s] Cloud Pro subscription. I'm very
[247.000s -> 249.000s] grateful Zed supports this flow because
[249.000s -> 251.000s] it seems like the agent provider is
[251.000s -> 254.000s] making money here, but presumably Zed is
[254.000s -> 257.000s] not. Meanwhile, Cursor is valued at $29
[257.000s -> 259.000s] billion, much of which seems
[259.000s -> 261.000s] attributable to its own internal agent.
[261.000s -> 262.000s] I don't know, man. I'm not Jim Kramer,
[262.000s -> 263.000s] but I'm probably missing something here.
[263.000s -> 266.000s] Anyway, yeah, ACP integrations is pretty
[266.000s -> 268.000s] huge. Right now, it looks like Cloud
[268.000s -> 270.000s] Code, Codeex, and Gemini are the ACP
[270.000s -> 273.000s] agents supported out of the box, but you
[273.000s -> 275.000s] can manually add others like Open Code
[275.000s -> 277.000s] on their website. Open code actually has
[277.000s -> 279.000s] instructions on how to add it in Zed as
[279.000s -> 281.000s] an external agent. By the time you watch
[281.000s -> 283.000s] this video, maybe Zed will have it as
[283.000s -> 285.000s] one of the default agents. You can also
[285.000s -> 287.000s] use Zed's internal agent, which can
[287.000s -> 288.000s] integrate with pretty much any OpenAI
[288.000s -> 290.000s] compatible inference provider, which
[290.000s -> 292.000s] does that mean I can use my beloved
[292.000s -> 294.000s] Cerebras as a coding agent in Zed? Why
[294.000s -> 297.000s] yes, yes, it does. And it is really,
[297.000s -> 300.000s] really fast. This footage is not sped up
[300.000s -> 302.000s] at all. I suspect all inference
[302.000s -> 304.000s] providers will eventually have this sort
[304.000s -> 307.000s] of speed, but until then, Cerebras is
[307.000s -> 309.000s] the leader in speed by a pretty
[309.000s -> 311.000s] ridiculous margin. Actually, I came to
[311.000s -> 313.000s] realize that I can use Cerebras through
[313.000s -> 315.000s] external ACP agents, too. I did feel
[315.000s -> 317.000s] like agent interaction went a little
[317.000s -> 319.000s] smoother with external agents as opposed
[319.000s -> 321.000s] to Zed's internal agent, but your
[321.000s -> 323.000s] mileage may vary. So, for me, I think
[323.000s -> 325.000s] the sweet spot might be using Cerebris
[325.000s -> 327.000s] models through Open Code as an external
[327.000s -> 329.000s] agent. Oh, and the beloved Olama is
[329.000s -> 331.000s] supported out of the box if you want to
[331.000s -> 333.000s] do inference locally. Pretty nice if you
[333.000s -> 335.000s] have some serious hardware and you want
[335.000s -> 337.000s] to go that route. There is a $10 a month
[337.000s -> 339.000s] ZP Pro subscription you can get. And I
[339.000s -> 341.000s] have some thoughts about this. It seems
[341.000s -> 343.000s] like the main value of Zed Pro comes
[343.000s -> 345.000s] down to two main things. First, you get
[345.000s -> 346.000s] all the Frontier models without having
[346.000s -> 348.000s] to deal with separate API keys and
[348.000s -> 350.000s] billing for each company. The second is
[350.000s -> 353.000s] the unlimited AIEit predictions, which
[353.000s -> 356.000s] is otherwise capped at 2,000 in the free
[356.000s -> 358.000s] tier. Here's the thing. You do get $5 of
[358.000s -> 361.000s] tokens included each month, but if you
[361.000s -> 363.000s] exceed that, you're paying per token
[363.000s -> 365.000s] just like you would without ZPro. Wait,
[365.000s -> 367.000s] actually you're paying 10% more than you
[367.000s -> 369.000s] would without ZP Pro. Don't get me
[369.000s -> 371.000s] wrong, there is value here depending on
[371.000s -> 373.000s] your situation, and it does negate the
[373.000s -> 375.000s] need for an external agent, but with
[375.000s -> 376.000s] what I know now, I don't think I'm
[376.000s -> 378.000s] personally going to be using this. And
[378.000s -> 380.000s] like I said, it's pretty cool of them to
[380.000s -> 381.000s] allow you to bring your own API key,
[381.000s -> 383.000s] even though it means they're making zero
[383.000s -> 384.000s] dollars off you. I know some of you are
[384.000s -> 386.000s] scared to work with AI, but maybe some
[386.000s -> 388.000s] of you are even more scared to work with
[388.000s -> 390.000s] humans. You might not like this feature,
[390.000s -> 392.000s] but it's actually pretty cool. It's
[392.000s -> 394.000s] called collabs and it's mainly intended
[394.000s -> 395.000s] for editing and discussing code
[395.000s -> 398.000s] together. There are channels and voice
[398.000s -> 399.000s] chat. You can invite your co-orker to
[399.000s -> 401.000s] your channels, then share the project
[401.000s -> 402.000s] you're working on with them. They can
[402.000s -> 404.000s] then read and write code anywhere in
[404.000s -> 406.000s] your project and you both get a
[406.000s -> 407.000s] real-time view of what the other person
[407.000s -> 409.000s] is doing. And then they can mess with
[409.000s -> 410.000s] you and just start cranking out Go code
[410.000s -> 412.000s] in the middle of your Rust file. Then
[412.000s -> 413.000s] you can right click on their name and
[413.000s -> 415.000s] choose revoke access. Now they can no
[415.000s -> 417.000s] longer edit your code. Jokes aside, this
[417.000s -> 419.000s] feature is pretty powerful and it isn't
[419.000s -> 421.000s] just limited to two people. You can have
[421.000s -> 423.000s] your entire team in here if you want to.
[423.000s -> 424.000s] That might be a lot of cooks in the
[424.000s -> 426.000s] kitchen, but if that's your thing, go
[426.000s -> 427.000s] for it. As I'm making this video, there
[427.000s -> 429.000s] is a Zed article near the top of
[429.000s -> 431.000s] HackerNews, and it's about how they use
[431.000s -> 433.000s] Zed's collab feature for most meetings.
[433.000s -> 435.000s] The CEO and co-founder of Zed is Nathan
[435.000s -> 438.000s] Sobo. Nathan actually worked on the Atom
[438.000s -> 440.000s] text editor while at GitHub, which was
[440.000s -> 442.000s] the first IDE built using the Electron
[442.000s -> 444.000s] framework, which at the time was built
[444.000s -> 446.000s] specifically for Atom. What else is
[446.000s -> 449.000s] built with Electron? VS Code and by
[449.000s -> 452.000s] extension cursor and anti-gravity. Zed
[452.000s -> 453.000s] was actually built on Electron early in
[453.000s -> 455.000s] the project, but apparently the team
[455.000s -> 457.000s] quickly realized it was putting too much
[457.000s -> 459.000s] of a damper on performance, so they
[459.000s -> 461.000s] wound up building their own UI framework
[461.000s -> 463.000s] in Rust. Make of that what you will.
[463.000s -> 464.000s] Anyway, overall, I had a positive
[464.000s -> 467.000s] experience with Zed. It is crazy fast.
[467.000s -> 470.000s] It is a joy to work with. Zed Pro seems
[470.000s -> 472.000s] meh, at least in its current form. Zed
[472.000s -> 474.000s] basically has all the agentic coding
[474.000s -> 475.000s] features you could want, including
[475.000s -> 477.000s] integration with pretty much any
[477.000s -> 479.000s] inference provider or external agent. At
[479.000s -> 481.000s] the time I'm making this video, I do
[481.000s -> 484.000s] plan to continue using Zed. Like I said,
[484.000s -> 485.000s] I'll be keeping a close eye on
[485.000s -> 487.000s] anti-gravity, but right now it's not
[487.000s -> 489.000s] there yet. I'm probably going to be
[489.000s -> 491.000s] canceling my cursor subscription,
[491.000s -> 492.000s] especially when I'm able to get a
[492.000s -> 494.000s] Cerebra subscription. At the time I'm
[494.000s -> 496.000s] making this video, you can't even get
[496.000s -> 498.000s] the coding plans. Presumably, they're
[498.000s -> 500.000s] overwhelmed with demand. I mean, I hate
[500.000s -> 502.000s] Cerebras and you should definitely not
[502.000s -> 505.000s] get a subscription. Jokes aside, Zed is
[505.000s -> 506.000s] worth checking out. It's free and open
[506.000s -> 508.000s] source. Thank you again to Zed for
[508.000s -> 510.000s] supporting the channel. Let me know what
[510.000s -> 512.000s] you think of Zed down in the comments,
[512.000s -> 514.000s] good or bad. I'd love to know if there's
[514.000s -> 516.000s] anything I'm overlooking. Thanks for
[516.000s -> 517.000s] watching and we'll see you in the next
[517.000s -> 520.000s] one.

COMMENTS:
1. [206 likes] @codeking4585: The best part of zed is that ultra fast and efficient, it almost eats no ram
2. [103 likes] @smrenatox: The best feature of Zed is the possibility of disable AI out of the box.
3. [101 likes] @benheidemann3836: Love Zed, I use it for pretty much everything now 😍 it’s so simple, uncomplicated, uncluttered and it feels really nice to use.
4. [85 likes] @alihasan167: Zed has less distractions as compared to vs code/cursor. It's unbelievable faster as compared to vs code.
5. [64 likes] @ouss: Zed + Claude Code + Convex = GOATED
6. [29 likes] @theintjengineer: Even when there was no Zed I used SublimeText. So, no VIM, Emacs, etc., but still.  Now, with Zed—bro, I can't leave it. It's just too good.  And they're also fast bringing in the latest AI Models haha
7. [22 likes] @hohohomeboy: I use Zed, and I really like it. It has a GUI, which may not be ideal for hardcore TUI fans. However, it is significantly faster and more memory-efficient than VSCode. The built-in AI feels different from some random VSCode extensions, and the ACP is fantastic. They are also developing a Rust GUI library, which is an exciting development. My only criticism is that the system prompts from Kilo Code are better. Yes, I can set up my own system prompts and profiles, but I believe reasonable defaults would be different.
8. [19 likes] @macaco_agiota: After using Zed, you can’t go back to any other editor.
9. [15 likes] @PaulSebastianManole: I tried it for a couple of months. Zed is closest to Neovim than anything else, OOB. That said, it forced me to use the mouse again, as not everything is keyboard-controllable. I just started being annoyed by that context switching and got mad urges to just to back to the terminal and my Neovim. And eventually I did and felt a huge relief. Like a weight had been lifted.
10. [10 likes] @ScottKohlmann: Videos are always great!
11. [8 likes] @Younex: I love using Zed it's so fast and instantaneous  All what I hope for is more extensions in the future
12. [8 likes] @TheRealisticNihilist: I'm just sad you left the church. But I'm not worried. You'll be back. They always come back.
13. [8 likes] @niacinsoupbowl: Zed is pretty good, I like the vim mode. But it not restoring unsaved files and work spaces is a deal break for myself when it comes to a GUI editor.
14. [8 likes] @AQMPolyface: I would use zed if helix did not exist.
15. [7 likes] @swordofthemorning777: Great video. With Zed being big on open source you can actually fix bugs/add requested features if you're good enough with Rust or open issues if you're not. The maintainers are very friendly and helpful.
16. [7 likes] @ghuxi: I think it's insane that Zed refuses to open any files other than proper UTF-8 encoded text files. Because of that, it could not replace even my text editor, let alone my IDE.
17. [5 likes] @Ephorr: Unfortunately I can't the moment you say Sponsored, all I can think of is an ad.
18. [4 likes] @TravisNuttall: I’ve been using zed for a while now, I still tend to drive coding agents in the terminal rather than in the agent panel, but ACP is awesome!
19. [4 likes] @oskarristolang: zed absolutely goated
20. [3 likes] : Best editor out there. Bar none.
21. [3 likes] @michael_gaio: “Zed is dead” ~ Pulp Fiction
22. [3 likes] @JesseJames-w1f: Neovim will always have my heart
23. [3 likes] @glyph6757: As both an emacs and a vim user I can not fathom why you'd want to use Zed over either.
24. [3 likes] @zx-sy1qh: A to Zed at the speed of Rust !
25. [3 likes] @sprightly106: it's funny that I found this channel because I was looking into the Glove80 but everything you cover perfectly aligns with my interests
26. [3 likes] @kevinmarsh1239: A bit off topic but I love your screen capture + zoom + tilt effect... so smooth! Can you share how you do that, or at least which app? Thanks!
27. [3 likes] @stefankyriacou7151: Wait, why are they charging a +10% premium to people who are already paying pro?
28. [3 likes] @ldov6373: Tried Zed just now, it didn't feel any faster or smoother than VS Code on Windows. Do you need a high refresh rate monitor to see the difference?
29. [2 likes] @monari_oj: Ive been using Zed since last year best IDE ever
30. [2 likes] @nonefvnfvnjnjnjevjenjvonej3384: Now you can try the real fast editor: Sublime Text.. About 10x faster than Zed on large files using multiple cursors..
31. [2 likes] @InternetEntreprenuer: They have made it way too bloated in the past year and they literally have a massive team committing to it everyday with Venture Capital. Yuck.
32. [2 likes] @hj.418: i too love zed but in my company laptop vdi there isn't even gpu😂 so i have to use sublime
33. [2 likes] @nicholasmanson8615: Thanks for the video. I dunno if ill leave emacs too but its pretty interesting.
34. [1 likes] @myfavouritecolorisgreen: zed's font rendering on linux doesn't seem to be great
35. [1 likes] @tsukinoko_kun: Zed has nearly the same issues as VS Code does. It's not extensible and builtin customization is extremely limited. But at least the performance is good I guess.
36. [1 likes] @nara_visuals: zen browser + zed editor
37. [1 likes] @Dr.Fox_90: Cursor needs to change their pricing, Antigravity is doing good, I am even sure that in 3-6 months they will polish it into something that is performing better.
38. [1 likes] @LastOne2Live: They need to redesign the extension market. It looks too basic and less informative.
39. [1 likes] @LuccDev: Wait, I thought you were using Neovim
40. [1 likes] @LampJustin: 2:26 whaaat, they have helix bindings??? I might give zed another try then! That's awesome!
41. [1 likes] @saeedxgholami: complicated ui with a lot of features. As a programmer we just need a compiler with good error reporting + a simple code editor.
42. [1 likes] @ruslanb6182: They don't have even block comments for selections, word wrap doesn't work good for laptops. Seems Zed is not production ready yet
43. [1 likes] @ibrahimsoukak437: Right except that it still lacks 100 of features. Half of VCS features are still missing. Refactoring is still very limited.
44. [1 likes] @ArtemMorinov: this is all very nice, but how do i turn on fps counter
45. [1 likes] @man-alive-q3n6q: So this is will be 4th editor/IDE for today -  Morning: Cursor Noon: Drop Cursor, you can use Kilo Extension on VS Code Afternoon: Did you try AntiGravity Evening: Zed Night: TBD
46. [1 likes] @Kiaulen: Zed is my goto editor. It's not my only editor (vs code/cursor still do a few things better, like markdown and js debugging), but it's wicked fast, there's a command for everything, completions work correctly, and the search is far and away the best out there.
47. [1 likes] @Gustafonair: I like the style of this video
48. [1 likes] @l7aromeo: Is the copy paste files fixed?
49. [1 likes] @JaFupy: I've been using Zed full time since June
50. [1 likes] @rct999: Is there any way to get those panel icon (explorer, search, git) on the left side like in VsCode?
51. [1 likes] @nico-l4o5h: is zed open source like vscode? so we can build from source our own zed editor, like vscodium for vscode? or its just some part of it that open source, so at the end its just ordinary proprietary software?  masya Allah, thanks you for the video :)
52. [1 likes] @sashogs: I switched to neovim years ago because of mouse stress, ram usage and speed, and Zed is now bringing me back out of the terminal. Still use Neovim but maybe 70/30. If Zed makes navigating around the ui using keyboard only, similar to Neovim then I’ll use it as my primary editor. I mostly use it for Claude code to show me what it’s changing and quickly navigate using mouse and especially large files.
53. [1 likes] @gauthier13: The collab feature might be the only thing who could eventually make me go away from neovim! Just kidding, my co-workers get layed off i work alone now...
54. [1 likes] @gavr_sas: Zed is 100% VSCode replacer for fast edit | pet projects | rare langs, but nobody will ever replace IDEA for production, since every other editor depends on LSP, and LSP cant integrate the frameworks u using with the language with ur database, typecheck ur SQL strings etc. Also framework specific inspections!  But yea, u need some RAM for that :)
55. [1 likes] @branislav3800: The Rust debugging is difficult to set up in Zed. It just hangs and doesn’t do anything. Cursor/VS Code debugging is easy to set up in
56. [1 likes] @pughums: Installed, Launched got this: The procedure entry point CreatePseudoConsole could not be located in the dynamically link library
57. [1 likes] @sunflash9: Helix mode all the way 😄.. waiting for 1.0 release and extensions support.
58. [1 likes] @TylerKoz: Is cerebras comparable to speed with groq?
59. [1 likes] @Silas2-p7c: Son, at some point, a roster gotta go back home and use vim.
60. [1 likes] @kinggrey2511: Emacs user but uses vim motions 99% of times (batman think) evil mode user
61. [1 likes] @lMINERl: Zed hummm bad no thanks, ima stick to to Terminal editors like Helix and Nvim, you need to see how fast they are before comparing them to zed, features? debuggers? Ai? all isnt an issue to integrate imho
62. [1 likes] @InternetEntreprenuer: It would be really cool if instead of constantly adding bloat features they made a cli tool like vim, that would be super awesome but im afraid too awesome to actually happen
63. [1 likes] @InternetEntreprenuer: The best theme (ive tried them all) by far is carbonfox
64. [1 likes] @amaan2025: havent watched the video yet but yes zed is goated, and no im not biased
65. [1 likes] @ronniemagatti3342: The only problem I have experienced with the share project feature is that for the user that is having a project shared with them, the Lsp completions are incredibly slow. Did you experience something similar when trying it out?
66. [1 likes] @hmziqrs: Antigravity doesn't even work. a few prompt and you hit your limit in 10 minutes on top of that it throws error in middle of chats and fucks up the flow.
67. [0 likes] @OpenSourceGuyYT: Did u tried warp terminal?
68. [0 likes] @scammerseason: Groq is faster
69. [0 likes] @DanteMishima: As soon as we get a Rename Matching Tag extension I'll fully switch
70. [0 likes] : ok sounds promising !  but i will stick to neovim
71. [0 likes] @Revanced-p9b: What extensiom did you used to make thos vertical lines visible? Like the one near the line number
72. [0 likes] @invranet: I dare say I have been using Zed since it was open-sourced. I have moved to Helix in the past year just because my workflow is more akin to "staying in the terminal and not leaving the terminal window." I  jumped out of my chair when I heard it had not only Vim mode, but now has a Helix mode?!? I still use Zed for collaboration with my friends because Helix has no plugin support (and that's what I like). I have always preferred Helix bindings over Vim after learning a few of them. I'm actually glad they merged in Helix key bind support because now I just feel at home, and don't need to relearn Vim bindings every single time I open Zed...
73. [0 likes] @dennisbarzanoff9025: aaaand no poper debugger
74. [0 likes] @ontanicolae1794: I just wish typescript was faster in it. And had a SQLServer extension
75. [0 likes] @ulrich-tonmoy: but one issue about extension is you cant see any preview/image or readme on the editor for that you need to go to github or its site
76. [0 likes] @omarmagdy1075: I mean ZED is objectively the best GUI editor the world isn't fair Cursor being valued as it is and Zed not. If I weren't too invested in my Neovim config and the muscle memory I have over the years I would definitely switch. I recommend Zed to everyone that doesn't want to learn Vim. The one thing that could make a big difference is accessible APIs to write plugins and extend the editor by the community
77. [0 likes] @lwuminhtris: Hey what's the font you are using on your Zed editor, thank you~
78. [0 likes] @laughingvampire7555: yes, emacs weak ass point is rendering is still 100% CPU.
79. [0 likes] @ytaccount9859: Can you share your cerebras set up / config with zed? Been trying to get it working like in your video but hitting big fails around structured output/response format/parallel tool calling and wondering if maybe I am dum
80. [0 likes] @Psoewish: I’m still really torn on zed, I checked it out because of the helix mode, but it has so many random quirks that really mess with me atm. Like how ‘gg’ goes to the first line, but not the actual start of the document. Like it’s a tiny thing but trips me up every time lol.
81. [0 likes] @anitshrestha8331: I hate the fact that I cannot display both the caret icon and the folder icon in sidebar. Besides that, yeah it is definitely faster than other IDEs I'm using.
82. [0 likes] @Faun471: I really like Zed. I use it for Flutter, web development and editing markdowns/json files.  A few days ago I tried how it would fare with a Java project and oh boy, did it absolutely fail.   I was not looking for a complete Intellij replacement, but I at least expected some level of parity with VSC + Java Extension Pack. I guess we're just not there yet (aside from the fact that Zed is probably not designed to be used that way anyway).
83. [0 likes] @matthieugindre1948: It's my favorite code editor with Cursor. Lighter, faster, very nice UI. The real advantage of Cursor to me is better edit predictions, their model is much smarter than Zed's.
84. [0 likes] @jricardoprog: Only work with utf8 files 😩....
85. [0 likes] @iamcasted: What has happened to our world.. In a video about IDEs more than 50% of speech is about LLMs and slop generators
86. [0 likes] @ArtemShoobovych: my take from this video: zed is a investors dream editor - 2/3 flashy but completely unnecessary features AND you get subscription for a yet another thing
87. [0 likes] @piotrw8989: Can we debug in zed now?
88. [0 likes] @slawtul: Two big features: AI and Colllab I am not interested in at all...
89. [0 likes] @sweetcapitan5690: Zed is:  1. Too stupid for fight with JB products.  2. Dont have enouht plugins for fight with VScode. 3. It is too fat and unconfigurable to compete with Vim.  2 year from release of Zed and only one mounth ago it released on Windows, apparently, AI functions are more "important" functionality.
90. [0 likes] @MeretheSolem: Current version of Zed fix all those problems they have with non built-in language support? C# and Java are barely usable in Zed just a few months ago, LSP servers constantly requiring restart, false positive errors warnings etc.
91. [0 likes] @Andy_B.: searching for a standalone ide, which is not affiliated wih the big AI companies.  thx
92. [0 likes] : I flip between neovim and zed these days.
93. [0 likes] @danishqureshi9414: I loved zed, The only thing keeping me me away from zed is spring development. I tried many things but just couldn't get jdtls and lombok running on zed with spring extensions. If someone knows it please let me know. For now unfortunately i m stuck with intellij
94. [0 likes] @nozwock: I should probably move to zed or just finally put my foot down on neovim (I just don't feel like messing with configs) since for some reason whenever I'm working on rust projects (actually it happens for non rust stuff too) vscode's performance continuously degrades (no idea why, system resources aren't capped or anything) until even moving the cursor lags, which leads me having to restart the editor.
95. [0 likes] @appuser: Why light themes? Because dark mode causes text to appear less sharp. We tend to spend too much time in low light levels, so I personally like to try to increase it when possible. Having white negative space does that. This could benefit vision, along with the additional blue light.
96. [0 likes] @PythonlyCode: 0:56 come on
97. [0 likes] @Tszyu01: My biggest issue was zed was lack of a debugger. It looks now it has the debugger built in, maybe it’s worth another shot.
98. [0 likes] @codem2022: Pricing model. Not worth spending time on Zed
99. [0 likes] @HorizonHuntxr: What mono font are you using?
100. [0 likes] @karthikeyanvj: no more helix?
101. [0 likes] @CripplingDuality: Private equity will inevitably turn Zed to shit, if prioritizing slopcoders didn't already set them down that path. That they chose to take blood money is all the worse.
102. [0 likes] @craig9668: Interesting overview. Apart from performance, going from Emacs to Zed looks like a real downgrade.
103. [0 likes] @zlk-zg3yj: You annoying
104. [0 likes] @ImranMunshi: Zed is an insane IDE, not sure why we need VS Code anymore, I can't deal with that sh8 anymore after being pleasantly Zed
105. [0 likes] @midlFidl: Zed is generally clean and fast but I found the built-in TS language server is very slow to respond compared to VS Code on large work projects.  I really like seeing errors show up and disappear quickly and this was pretty disappointing.
106. [0 likes] @NathanMcCoyTheFirst: Zed is ace! Fast, uncluttered - and new features are showing up every week.   I use git worktrees and they just added a command palette to switch worktrees, either in a new window or in the current - something I didn’t know I wanted and there it is and very useful. It’s a trivial example and only saves a few keystrokes but it’s a good example of their continuous improvement.   When I started using zed they didn’t have a git panel but it was soon added and now I like it more than the one I used to used in IDEA.    Settings used to be only in json - but now there is also a fast, searchable panel.    Zed’s the ed for me.
107. [0 likes] @UwU-dx5hu: How did you open the settings panel? I am tired of editing the settings json file
108. [0 likes] @erdhyernando: is this sign to finally try zed?
109. [0 likes] @lynxslove7495: how to fix this HTTP response error from Zed's API: status 451 Unavailable For Legal Reasons - "Access to Anthropic models is not available from this data center (HKG)"
110. [0 likes] @SoftaPen: yeeeeeeeeeeeeeees yeeeeeeeeeeeeeeeeeeeeeees finally some one talking of zed now lol.. also lemme tell you zed is now abiliable for windows ; is the exe ,  not binary build
111. [0 likes] @voodookiidoo: zed is like is a great ide for langs such as rust/go i hope they will make a public release of their gui lib (it is still opened, but the lack of docs makes it unfun to use), and define a plugins system, so the community could bring it's functionality on a new level
112. [0 likes] @mykemperor458: For me zed is not good because it does not support c++ code navigation out of the box like 10x does.
113. [0 likes] @happydev512: I can not use java efficently in ZED
114. [0 likes] @superresistant0: I wanted to see tests with gpt 5.1 and gemini 3.
115. [0 likes] @VadimSuharnikov: Zed is a really good editor. But I prefer VS Code and its clones because they have LLM sessions.
116. [0 likes] @iliyalb: i use lm studio with zed, it seems many models that have been trained for tool use struggle to work in zed. the only models i have had success with were gpt-oss and devstral.
117. [0 likes] @mednson: What I don't like about it is that I can't see data types of variables like how I see in VScode I have researched it almost but the solutions I've found don't work😒
118. [0 likes] @DaKingof: I mean, you could have added that the subscriptions are more for supporting the devs instead of just saying they are `meh`. Kind of a slap in the face if we are being real here.
119. [0 likes] @mirkofacose: I've been using only VScode for the past year to write my code in Rust... But your video convinced me to try Zed out! You'll hear from me if I don't like it.... or if I do! 😜
120. [0 likes] @razorree: does it work like Antigravity? does it have good integration with Claude4.5 or Gemini2.5 or 3 ?. how about Kotlin or Java ?
121. [0 likes] @ЕвгенийКрасилов-о9о: Cons I encounered: - Git is not cooked properly yet. Doesn't really matter if you are terminal god. - It still immature. Expect bugs and flow breaks. It's very bad to suddenly realize that debugger is broken or type checker is not updating. Expect this, do not uninstall your main code editor or be ready to roll back to previous versions. - Couldn't run local AI model for autocompletions using llama.cpp server. Only chat... Though they have support of supermaven and some other providers. Still, not a big fan of sourcing my code to external services... I just hope I'm a dogshit programmer and my code has no value for them😂 - At this point it kinda nitpicking, but importing other editor (VSCode) keybinding is not fully 1 to 1. For example, Alt + Left/Right arrow is now Alt + -/+. Arguably it doesn't matter because if you care about your tools, you will tweak your keybindings and settings.  But pros are really valuable. Good performance, not bloated ram usage, really good out of the box tools. Python with basedpyright by default? Hell yeah! I didn't even know about this lsp, pyright was my world. And I wait until `ty` (supported out of the box too) will be mature enough. Rust-analyzer is here too. And several other languages are supported by the team.  Overall pretty much rock solid editor with high bar for basic features (lsp, formatters included) and good performance and resources usage but lacking a *good* Git panel and expect critical workflow bugs from time to time.