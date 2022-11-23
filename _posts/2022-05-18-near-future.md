---
layout: post
title: Near Future
image: 
---

What I've shipped:
Nothing :(

What I'm working on:
Text prompt to generated visuals audio responsive videos

What I see in the near-future:
Movies that are incorporate on-the-fly generated assets from genre, themes, specific actors/locales/time periods

Dream journals with automated visuals - topic model sentences to grab the most important text, create visuals, mint journal entry?

Language learning through conversation and real-time transcription. Ex. Spanish learner stumbles in conversation and switches back to English for a few words - transcription software notes down the english and marks as new vocabulary.


## What will change in the near-future?

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">“A Shiba Inu dog wearing a beret and black turtleneck” <a href="https://twitter.com/hashtag/dalle?src=hash&amp;ref_src=twsrc%5Etfw">#dalle</a> <a href="https://t.co/VkAsZsNMhY">pic.twitter.com/VkAsZsNMhY</a></p>&mdash; OpenAI (@OpenAI) <a href="https://twitter.com/OpenAI/status/1511714516345651204?ref_src=twsrc%5Etfw">April 6, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Context - 

with iterations in text to image generation it might be possible within the next few years to generate movies from stories

### Current tools to generate images from text and how I'm working with them.

**VQGAN + CLIP**

GANs (Generative Adversarial Networks) are systems where two neural networks are pitted against one another: a generator which synthesizes images or data, and a discriminator which scores how plausible the results are. The system feeds back on itself to incrementally improve its score.


CLIP (Contrastive Language–Image Pre-training) is a companion third neural network which finds images based on natural language descriptions, which are what’s initially fed into the VQGAN.

[helpful tutorial](https://heystacks.com/doc/935/introduction-to-vqganclip)

[colab link to run it](
https://colab.research.google.com/github/justinjohn0306/VQGAN-CLIP/blob/main/VQGAN%2BCLIP(Updated).ipynb#scrollTo=g7EDme5RYCrt)


**CogView**

[CogView](https://github.com/THUDM/CogView)

These notebooks + following along with this tutorial by [Lia Coleman](https://www.youtube.com/watch?v=97aRnMU3Cgs&ab_channel=Babycastles) to create a beat detector along with video in TouchDesigner will eventually lead to generated visual videos for mixes. Somewhere along the way, I want to add custom trained StyleGanADA model to "walk" along different images, creating a video to use for audio modulation. 