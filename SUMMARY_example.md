### Video Content Summary
This video presents a first-impressions review of the Zed code editor from the perspective of a developer with a background in Emacs and recent experience with Cursor. The creator notes the sponsorship but asserts it will not influence their opinions. The review covers Zed's core philosophy of performance, demonstrated by its 120 FPS UI and Rust-based architecture, which the creator argues results in a noticeably faster experience than Electron-based alternatives like VS Code and Cursor. A significant portion is dedicated to Zed’s approach to AI-assisted coding, specifically its Agent Communication Protocol (ACP), which allows integration with external AI agents like Claude Code and Open Code, offering flexibility over locked-in solutions. The creator also explores features like Vim/Helix modes, extension installation speed, and real-time collaboration, while offering a critical analysis of the Zed Pro subscription model. The narrative concludes with the creator's intent to switch from Cursor to Zed, citing its speed, open-source nature, and flexible AI integrations as key advantages, despite some reservations about the Pro tier.

### Key Insights
- **Performance as a Core Tenet** (Time: 01:10): The creator argues that Zed's dedication to optimal performance, including a 120 FPS UI and a custom Rust-based framework, makes it feel "instantaneous" and significantly faster than Electron-based editors like VS Code.
- **Flexible AI Integration via ACP** (Time: 03:32): The reviewer highlights Zed's Agent Communication Protocol (ACP) as a major differentiator, which allows users to integrate various external AI agents (e.g., Claude Code, Open Code) using existing subscriptions, contrasting it with Cursor's closed, proprietary agent model.
- **Critical View of Zed Pro** (Time: 05:37): The creator expresses a negative opinion of the Zed Pro subscription, questioning its value proposition due to a 10% markup on token costs beyond the included $5 monthly credit and the capped AI predictions in the free tier.

### Detailed Breakdown
| Feature / Aspect | Details / Verdict |
|---|---|
| **Performance & Architecture** | Built in Rust on a custom UI framework for maximum speed and low resource usage; creator claims it feels faster than VS Code/Cursor. |
| **AI & Coding Assistance** | Supports ACP for external agents (Claude Code, Open Code) and an internal agent for OpenAI-compatible providers; AI edit predictions are on par with Copilot. |
| **Editor Features** | Includes Vim mode with surround motions and Helix mode; supports common VS Code keybindings; fast extension installation. |
| **Collaboration (Collabs)** | Real-time multi-user editing with project sharing, channels, and voice chat, noted as a powerful feature for teams. |
| **Pricing Model** | Free tier is capable; Zed Pro subscription ($10/month) offers Frontier models and unlimited predictions, but creator deems it underwhelming due to token pricing structure. |

### Community Intelligence
**Overall**: The sentiment is overwhelmingly Positive, with widespread praise for Zed's speed and efficiency. A minority of comments express strong preferences for terminal-based editors (Neovim, Helix) or highlight specific missing features.

**Positive Highlights**:
- **Performance & Efficiency**: Multiple users praise Zed for being "unbelievably faster" and using significantly less RAM than VS Code. (approx 206+ likes)
- **Simplicity & Design**: Users appreciate its uncluttered interface and the feeling of being a "joy to use." (approx 103 likes)
- **AI Flexibility**: The ability to disable AI entirely or use external agents via ACP is highlighted as a major benefit. (approx 103 likes)

**Criticisms/Negatives**:
- **Keyboard-Centric Workflows**: Some users, particularly from Neovim/Helix backgrounds, criticize that not all UI elements are keyboard-controllable, forcing mouse use. (approx 15 likes)
- **Missing Features**: Comments note the lack of certain features like robust unsaved file restoration (disputed by another user), limited VCS integration, and difficulty with Rust debugging. (approx 8-15 likes)

**Community Knowledge (Corrections, Disputes, & Tips)**
- **[Dispute/Clarification]**: User @panstromek disputes the claim that Zed does not restore unsaved buffers, stating they have "tens of unsaved files perma-opened" that are restored after a restart.
- **[Additive Tip]**: User @hohohomeboy suggests that while ACP is fantastic, the system prompts from "Kilo Code" are better, though custom profiles can be set up in Zed.
- **[Technical Clarification]**: User @ghuxi provides a detailed correction regarding file encoding, explaining that Zed rejects non-UTF-8 files (like ISO-8859-1 or UTF-16), which is a known limitation and the subject of GitHub issues.

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
... (truncated if too long)

COMMENTS:
1. [206 likes] @codeking4585: The best part of zed is that ultra fast and efficient, it almost eats no ram
2. [101 likes] @smrenatox: The best feature of Zed is the possibility of disable AI out of the box.
3. [101 likes] @benheidemann3836: Love Zed, I use it for pretty much everything now 😍 it’s so simple, uncomplicated, uncluttered and it feels really nice to use.
4. [85 likes] @alihasan167: Zed has less distractions as compared to vs code/cursor. It's unbelievable faster as compared to vs code.
5. [64 likes] @ouss: Zed + Claude Code + Convex = GOATED
6. [29 likes] @theintjengineer: Even when there was no Zed I used SublimeText. So, no VIM, Emacs, etc., but still.  Now, with Zed—bro, I can't leave it. It's just too good.  And they're also fast bringing in the latest AI Models haha
7. [22 likes] @hohohomeboy: I use Zed, and I really like it. It has a GUI, which may not be ideal for hardcore TUI fans. However, it is significantly faster and more memory-efficient than VSCode. The built-in AI feels different from some random VSCode extensions, and the ACP is fantastic. They are also developing a Rust GUI library, which is an exciting development. My only criticism is that the system prompts from Kilo Code are better. Yes, I can set up my own system prompts and profiles, but I believe reasonable defaults would be different.
8. [19 likes] @macaco_agiota: After using Zed, you can’t go back to any other editor.
9. [17 likes] @codetothemoon: Agree this is a huge perk!
10. [15 likes] @PaulSebastianManole: I tried it for a couple of months. Zed is closest to Neovim than anything else, OOB. That said, it forced me to use the mouse again, as not everything is keyboard-controllable. I just started being annoyed by that context switching and got mad urges to just to back to the terminal and my Neovim. And eventually I did and felt a huge relief. Like a weight had been lifted.
11. [10 likes] @thecriticizedgamer8508:  @pranav-jr3iu  Yes because nvim has lua embedded but zed extensions are written in rust and are compiled to web asm.
12. [10 likes] @ScottKohlmann: Videos are always great!
13. [8 likes] @Younex: I love using Zed it's so fast and instantaneous  All what I hope for is more extensions in the future
14. [8 likes] @TheRealisticNihilist: I'm just sad you left the church. But I'm not worried. You'll be back. They always come back.
15. [8 likes] @niacinsoupbowl: Zed is pretty good, I like the vim mode. But it not restoring unsaved files and work spaces is a deal break for myself when it comes to a GUI editor.
16. [8 likes] @AQMPolyface: I would use zed if helix did not exist.
17. [8 likes] @Adithya-ih8fi: ​ @malhashemi90 I think he's talking about people who actually do something productive other than just flexing they use nvim.
18. [7 likes] @J-Kimble: +1
19. [7 likes] @markmywords3817: This is the only reason why I keep sublime text around 😂  VS Code is too slow  I've been using Vim 8 and neovim for a long time I'm entrenched in my whole custom config already.  But Zed just might replace my Sublime Text install 😅
20. [7 likes] @ghuxi: I think it's insane that Zed refuses to open any files other than proper UTF-8 encoded text files. Because of that, it could not replace even my text editor, let alone my IDE.
21. [7 likes] @thedeemon: "Restore unsaved buffers" is in the options
22. [7 likes] @codetothemoon: I’m loving it so far too… currently no plans to switch to anything else. Biggest contender for me right now is probably Neovim
23. [7 likes] @codetothemoon: Nice, I haven’t tried Convex! Will check out…
24. [6 likes] @swordofthemorning777: Great video. With Zed being big on open source you can actually fix bugs/add requested features if you're good enough with Rust or open issues if you're not. The maintainers are very friendly and helpful.
25. [6 likes] @codetothemoon: agree 100%
26. [5 likes] @Ephorr: Unfortunately I can't the moment you say Sponsored, all I can think of is an ad.
27. [5 likes] @codetothemoon: Agree 100% it's pretty good. and Sublime was great back in the day!
28. [5 likes] @malhashemi90: Let me correct that Neovide+OpenCode+Convex+Sveltekit=GOATED
29. [4 likes] @TravisNuttall: I’ve been using zed for a while now, I still tend to drive coding agents in the terminal rather than in the agent panel, but ACP is awesome!
30. [4 likes] @JohnWeakReference: im using gpui to build nativechat which is alternative to openwebui , would probably open source it later this yearend, but yeah GPUI is Zed Industries open source
31. [4 likes] @oskarristolang: zed absolutely goated
32. [4 likes] @codetothemoon: Helix is fantastic!
33. [3 likes] : Best editor out there. Bar none.
34. [3 likes] @michael_gaio: “Zed is dead” ~ Pulp Fiction
35. [3 likes] @krazymeanie: ​ @MugiwaraNoDeji I'm sorry if you need AI to get shit done but some people don't. That's why
36. [3 likes] @JesseJames-w1f: Neovim will always have my heart
37. [3 likes] @glyph6757: As both an emacs and a vim user I can not fathom why you'd want to use Zed over either.
38. [3 likes] @zx-sy1qh: A to Zed at the speed of Rust !
39. [3 likes] @sprightly106: it's funny that I found this channel because I was looking into the Glove80 but everything you cover perfectly aligns with my interests
40. [3 likes] @codetothemoon: its MUCH faster actually! Groq is a solid #2, but Cerebras has a pretty big lead over them
41. [3 likes] @kevinmarsh1239: A bit off topic but I love your screen capture + zoom + tilt effect... so smooth! Can you share how you do that, or at least which app? Thanks!
42. [3 likes] @codetothemoon: Interesting, I haven't heard of Kilo Code - thanks for putting it on my radar!
43. [3 likes] @codetothemoon: understandable! I am a habitual saver so I actually didn't notice this. Kind of surprising, seems like an easy feature to implement!
44. [3 likes] @stefankyriacou7151: Wait, why are they charging a +10% premium to people who are already paying pro?
45. [3 likes] @jwllzp: except nvim ;)
46. [3 likes] @ldov6373: Tried Zed just now, it didn't feel any faster or smoother than VS Code on Windows. Do you need a high refresh rate monitor to see the difference?
47. [3 likes] @iatheman:  @codetothemoon  And it uses way less resources. The only thing VS Code has on it is the colossal amount of plugins.
48. [3 likes] @nicholasmanson8615: Wots convex?
49. [2 likes] @monari_oj: Ive been using Zed since last year best IDE ever
50. [2 likes] @pranav-jr3iu: Compared to nvim?
51. [2 likes] @julioflores1849: I only use zed and I can say that that’s not true. Ive seen my usage go over 1gb but that’s because I’ve had many editors open with many many tabs😊
52. [2 likes] @nonefvnfvnjnjnjevjenjvonej3384: Now you can try the real fast editor: Sublime Text.. About 10x faster than Zed on large files using multiple cursors..
53. [2 likes] @codetothemoon: thanks! its actually mCamRig from MotionVFX! One of their completely free plugins actually: https://www.motionvfx.com/store,mcamrig,p2219.html?srsltid=AfmBOoprEUtujvO1vyof_UfyiSGhFR7f9kCTIihvkrQ2UxeWX26Gdqd8
54. [2 likes] @codetothemoon: haha I may be back! Still love Emacs
55. [2 likes] @panstromek: It does for me? I have tens of unsaved files perma-opened in there. It always brings them back after restart.
56. [2 likes] @codetothemoon: i love cli tools too! unfortunately a huge segment of the market is averse to them still, so im guessing its difficult to build a business around an ide that is terminal based
57. [2 likes] @InternetEntreprenuer: They have made it way too bloated in the past year and they literally have a massive team committing to it everyday with Venture Capital. Yuck.
58. [2 likes] @pheenty: Zed has helix mode built-in, alongside vim mode
59. [2 likes] @hj.418: i too love zed but in my company laptop vdi there isn't even gpu😂 so i have to use sublime
60. [2 likes] @codetothemoon: ahh thanks for pointing this out! actually I am not sure, sadly I didn't have anyone to help me test it so I was going back and forth between two computers lol
61. [2 likes] @codetothemoon: Agree 💯
62. [2 likes] @nicholasmanson8615: Thanks for the video. I dunno if ill leave emacs too but its pretty interesting.
63. [2 likes] @codetothemoon: Thank you!
64. [2 likes] @codetothemoon: I have a 60hz monitor and an m4 Mac Studio and the difference is noticeable. Not quite “night and day”, but it is there
65. [1 likes] @myfavouritecolorisgreen: zed's font rendering on linux doesn't seem to be great
66. [1 likes] @tsukinoko_kun: Zed has nearly the same issues as VS Code does. It's not extensible and builtin customization is extremely limited. But at least the performance is good I guess.
67. [1 likes] @codetothemoon: what sort of customization are you looking for? I don't know what constraints are imposed on plugins as compared to something like Neovim plugins
68. [1 likes] @nara_visuals: zen browser + zed editor
69. [1 likes] @Dr.Fox_90: Cursor needs to change their pricing, Antigravity is doing good, I am even sure that in 3-6 months they will polish it into something that is performing better.
70. [1 likes] @cassolmedia: I suspect at that point the pricing will reach parity with cursor.  This is how it always starts
71. [1 likes] @LastOne2Live: They need to redesign the extension market. It looks too basic and less informative.
72. [1 likes] @LuccDev: Wait, I thought you were using Neovim
73. [1 likes] @codetothemoon: I do use it occasionally, but it’s never really been my go to IDE. I did use it to write the script for this video though!
74. [1 likes] @LampJustin: 2:26 whaaat, they have helix bindings??? I might give zed another try then! That's awesome!
75. [1 likes] @saeedxgholami: complicated ui with a lot of features. As a programmer we just need a compiler with good error reporting + a simple code editor.
76. [1 likes] @ruslanb6182: They don't have even block comments for selections, word wrap doesn't work good for laptops. Seems Zed is not production ready yet
77. [1 likes] @ibrahimsoukak437: Right except that it still lacks 100 of features. Half of VCS features are still missing. Refactoring is still very limited.
78. [1 likes] @ArtemMorinov: this is all very nice, but how do i turn on fps counter
79. [1 likes] @man-alive-q3n6q: So this is will be 4th editor/IDE for today -  Morning: Cursor Noon: Drop Cursor, you can use Kilo Extension on VS Code Afternoon: Did you try AntiGravity Evening: Zed Night: TBD
80. [1 likes] @Kiaulen: Zed is my goto editor. It's not my only editor (vs code/cursor still do a few things better, like markdown and js debugging), but it's wicked fast, there's a command for everything, completions work correctly, and the search is far and away the best out there.
81. [1 likes] @Gustafonair: I like the style of this video
82. [1 likes] @codetothemoon: Great, thanks for letting me know! It really helps me decide how approach future videos
83. [1 likes] @l7aromeo: Is the copy paste files fixed?
84. [1 likes] @JaFupy: I've been using Zed full time since June
85. [1 likes] @rct999: Is there any way to get those panel icon (explorer, search, git) on the left side like in VsCode?
86. [1 likes] @nico-l4o5h: is zed open source like vscode? so we can build from source our own zed editor, like vscodium for vscode? or its just some part of it that open source, so at the end its just ordinary proprietary software?  masya Allah, thanks you for the video :)
87. [1 likes] @pookiepats: Happy for you
88. [1 likes] @D-Oliver: What kind of things aren't controllable with the keyboard? (VS Code + Vim extension here atm, considering Neovim and Zed.)
89. [1 likes] @sashogs: I switched to neovim years ago because of mouse stress, ram usage and speed, and Zed is now bringing me back out of the terminal. Still use Neovim but maybe 70/30. If Zed makes navigating around the ui using keyboard only, similar to Neovim then I’ll use it as my primary editor. I mostly use it for Claude code to show me what it’s changing and quickly navigate using mouse and especially large files.
90. [1 likes] @codetothemoon: you can go keyboard only! Most critical functionality has default keybindings, though there is some that does not. But I have not found a piece of functionality for which a keybinding cannot be assigned. That said, Neovim is fantastic 😎
91. [1 likes] @gauthier13: The collab feature might be the only thing who could eventually make me go away from neovim! Just kidding, my co-workers get layed off i work alone now...
92. [1 likes] @gavr_sas: Zed is 100% VSCode replacer for fast edit | pet projects | rare langs, but nobody will ever replace IDEA for production, since every other editor depends on LSP, and LSP cant integrate the frameworks u using with the language with ur database, typecheck ur SQL strings etc. Also framework specific inspections!  But yea, u need some RAM for that :)
93. [1 likes] @codetothemoon: nice, super glad to hear this! I am always thinking about the folks who love the coding but hate the keyboards, and vice versa. Really happy to know that the overlap exists!
94. [1 likes] @codetothemoon: Understandable, but if you watch the rest of the video it'll become very apparent I'm giving my honest opinion (spoiler: Zed Pro is not the best)
95. [1 likes] @branislav3800: The Rust debugging is difficult to set up in Zed. It just hangs and doesn’t do anything. Cursor/VS Code debugging is easy to set up in
96. [1 likes] @pughums: Installed, Launched got this: The procedure entry point CreatePseudoConsole could not be located in the dynamically link library
97. [1 likes] @sunflash9: Helix mode all the way 😄.. waiting for 1.0 release and extensions support.
98. [1 likes] @TylerKoz: Is cerebras comparable to speed with groq?
99. [1 likes] @twenty-fifth420: I am sorry to fact check you, but are you sure this is accurate? my language of choice is Ada which encodes files/strings as ascii (yes it is that old) and it works fine. Was it using UTF-8 in like a markdown file? Or was it just using a language that only has UTF-8? I am slightly confused and I would to like what you mean if you can explain.
100. [1 likes] @ghuxi: 7-bit ascii is valid UTF-8. UTF-8 was made to be backward compatible with ascii files. But.. if you try to open for example a ISO-8859-1 file that uses codepoints between 128 and 255 it will just say "could not open file". Other latin encodings, UTF-16, Windows 1252 would also fail miserably. Don't even dream about sneak peeking into a binary or a file with custom header.  There've been feature requests for years about it, the current one with example files is issue #16965 on github.