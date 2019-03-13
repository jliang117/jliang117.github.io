---
layout: post
title: Sample Sales
image: /img/choosybeg.png
---

I check out NYC samples sales occasionally - a good resource has been [The Choosy Beggar](http://thechoosybeggar.com).
I had a problem with the way  the site separated each sale post and their respective maps, 
meaning I'd go through multiple clicks back and forth to view each location, and couldn't plan my 
route very well. 
I realized that figuring out the route was much easier when I could visualize all the pins on one map, 
so the idea was to scrape the site for sales, generate json map pins, and place them on a static map:

[check it out here](../sampleSaleProject/sampleSaleMapNYC.html)

The content is stored in `pins.json`, and a typical pin looks like:

    {
    	title:"",
    	longtitude:"-74.0016897",
    	latitude:"40.7214286",
    	description: "James Perse Weekdays Mon-Thurs 10-6"
    }

There's a TravisCI daily cronjob that runs the update script and commits the new json file, so this works fairly well!

A useful addition might be to add a hyperlink to the description to the original sale, maybe when I have some extra time...