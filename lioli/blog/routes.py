from flask import render_template,Blueprint
from sqlalchemy import desc

blog_bp = Blueprint('blog',__name__)


@blog_bp.route("/blogs-by-lioli-ceramica/")
def blog():
    return render_template('blog.html',title="Latest Blogs by Lioli Ceramic on Porcelain Tiles, Ceramic Tiles & In-General Discussion of Ceramic World",desc="Are you looking for insightful articles on porcelain slab manufacturing, tile manufacturing, and in-general ceramic world insights? Well, Lioli Ceramica shares critical insights on similar topics quite frequently here.")

@blog_bp.route("/blog/how-to-keep-bathroom-floor-dry/")
def blog_inside():
    return render_template('blog-inside.html',title="How to Keep Bathroom Floor Dry | Anti-Slip Bathroom Floor",desc="How to keep bathroom floor dry; this article on making an anti-slip bathroom floor will help you understand the process to keep the bathroom floor dry efficiently.")

@blog_bp.route("/blog/kitchen-countertops-design-inspirations-by-lioli-ceramica/")
def blog_inside2():
    return render_template('blog-inside-2.html',title="Kitchen Countertops Design Inspiration of 2022 by LioliCeramica",desc="Are you looking for kitchen countertops design inspiration to remodel your kitchen with a 2022 aesthetic and pleasing look? LioliCeramica shares the kitchen countertop's design inspiration for 2022 and beyond in this article.")


@blog_bp.route("/blog/why-porcelain-tiles-are-better-than-natural-stones/")
def blog_inside3():
    return render_template('blog-inside-3.html',title="Why Porcelain Tiles are Better Than Natural Stones (Marble, Quartz &, etc.)",desc="Why porcelain tiles are better than natural stones in general, this article helps understand the benefits of choosing porcelain tiles over natural stones.")


@blog_bp.route("/blog/porcelain-tiles-vs-ceramic-tiles/")
def blog_inside4():
    return render_template('blog-inside-4.html',title="Porcelain Tiles vs Ceramic Tiles; Comparison to Find Which one is Better!",desc="Porcelain tiles vs ceramics tiles, it's a big question for many; this article will give you a brief comparison between choosing porcelain tiles or ceramic tiles, followed by which one performs better for long-term durability & aesthetic.")



@blog_bp.route("/blog/how-to-clean-porcelain-tiles/")
def blog_inside5():
    return render_template('blog-inside-5.html',title="How To Clean Porcelain Tiles",desc="Porcelain is a highly durable flooring that doesn't need much maintenance and cleaning. Boasting the attributes of being scratch, stain, and water-resistant, installing porcelain tiles provides an advantage over other non-porcelain tiles. However, you would still like it to look its best, don't you?")


@blog_bp.route("/blog/how-to-clean-grout/")
def blog_inside6():
    return render_template('blog-inside-6.html',title="How To Clean Grout: 7 Efficient Ways To Renew Old Grout As New",desc="Tiles are beautiful, sturdy, and have the best floors and wall options. It gets dirty and even cleaned with just minor efforts. But, the Grout! While tiles are the easiest to clean, grout isn’t. You need to spend your lovely afternoon cleaning those greasy lines between your tiles.")


@blog_bp.route("/blog/choose-the-right-tiles-for-your-office/")
def blog_inside7():
    return render_template('blog-inside-7.html',title="Choose The Right Tiles For Your Office: A Complete Guide",desc="Your office space flooring is integral to representing your brand, working style, and company image. Choosing the right office floor tiles design may sound like a chore, but a simple mistake causes nuisance later and can make you lose a chunk of money.")


@blog_bp.route("/blog/an-ultimate-guide-on-large-format-porcelain-tiles/")
def blog_inside8():
    return render_template('blog-inside-8.html',title="An Ultimate Guide on Large Format Porcelain Tiles",desc="Large format porcelain tiles- get to know everything about porcelain slabs. Read on to know more about big-sized porcelain slabs- installation, benefits, sizes, and more!")



@blog_bp.route("/blog/lioli-complete-guide-choosing-the-right-tiles-for-outdoor-space/")
def blog_inside9():
    return render_template('blog-inside-9.html',title="Lioli’s complete guide to choosing the right tiles for outdoor space",desc="Selecting the right tiles can be a daunting task. Read our guide on how to choose the right tile for your outdoor space to make your exterior look elegantly stunning!")


@blog_bp.route("/blog/large-format-porcelian-tiles-10-reasons-to-consider-them/")
def blog_inside10():
    return render_template('blog-inside-10.html',title="Large Format Porcelain Tiles: 10 Reasons to Consider Them",desc="Large format porcelain tiles are becoming extremely popular in residential and office spaces. Let’s explore the benefits of using large format porcelain tiles. ")




@blog_bp.route("/blog/get-your-home-festive-ready-with-lioli-ceramica/")
def blog_inside11():
    return render_template('blog-inside-11.html',title="THIS DIWALI, GET YOUR HOME FESTIVE-READY WITH LIOLI CERAMICA",desc="Wow your guests with porcelain tile; get your home festive-ready with Lioli Ceramica. This Diwali, add a touch of colour, love, and charm to your space with Lioli’s wide range of porcelain slab collections for different spaces.")


@blog_bp.route("/blog/everything-you-need-to-know-about-porcelain-tiles/")
def blog_inside12():
    return render_template('blog-inside-12.html',title="Everything You Need To Know About Porcelain Tiles",desc="Porcelain tiles are durable and stronger tiling material. This blog contains everything you need to know about porcelain tiles; from their type to their benefits, this guide provides it all!")


@blog_bp.route("/blog/lioli-6-warms-tips-to-winterize-your-living-room/")
def blog_inside13():
    return render_template('blog-inside-13.html',title="LIOLI’S 6 WARM TIPS TO WINTERIZE YOUR LIVING ROOM ",desc="Is your living room ready to face winter? Lioli presents six simple tips to make your living room a comfortable place and lend it a cosy, warm, and alluring vibe with our marvellous porcelain tile collection. ")



@blog_bp.route("/blog/15-useful-tips-to-find-the-perfect-tiles-for-your-home/")
def blog_inside14():
    return render_template('blog-inside-14.html',title="15 USEFUL TIPS TO FIND THE PERFECT TILES FOR YOUR HOME",desc="What to keep in mind when selecting tiles for your home? Read our guide on 15 tips to choose the perfect tiles for your home; it will help you get the right tile for every space.")




@blog_bp.route("/blog/the-5-best-tips-for-maintaining-porcelain-tiles-in-winter/")
def blog_inside15():
    return render_template('blog-inside-15.html',title="The 5 Best Tips For Maintaining Porcelain Tiles In Winter: Edition 2022",desc="Winter can prove tough for floor surfaces. Hence, this article explains some helpful tips to clean and maintain your porcelain tiles this winter.")






@blog_bp.route("/blog/installation-guide-for-large-format-porcelain-tiles/")
def blog_inside16():
    return render_template('blog-inside-16.html',title="Installation Guide for Large Format Porcelain Tiles",desc="Large-format porcelain tiles are stunning tiles that can be tricky to lay due to their size and heavy material. This guide will discuss the tile installation process and some extra precautions you might want to avoid while installing large-format tiles.")




@blog_bp.route("/blog/2023-tile-trend-look-out-for-immersive-feel-and-look/")
def blog_inside17():
    return render_template('blog-inside-17.html',title="2023 Tile Trends to Look out for Immersive Feel & Look",desc="Discover the latest tile trend in 2023 for an immersive look and feel. From traditional stone look tile to classy tile schemes, add a sense of touch to your home decor. ")

@blog_bp.route("/blog/branded-vs-local-tiles-which-is-the-best-flooring-option/")
def blog_inside18():
    return render_template('blog-inside-18.html',title="Branded Vs Local Tiles: Which Is The Best Flooring Option?",desc="Having trouble deciding between branded and local tiles? These both look the same from the exterior but are miles apart. Read the blog to know the difference between branded and local tiles and which option is better for your home. ")





@blog_bp.route("/blog/bring-your-space-to-life-with-stone-look-porcelain-tile/")
def blog_inside19():
    return render_template('blog-inside-19.html',title="Bring Your Space To Life With Stone-Look Porcelain Tile",desc="Looking for some aesthetic changes to your floor tiles? Try stone-look porcelain stoneware floor tiles. Here is our complete guide: stone look porcelain floor tiles and enhance the beauty of your space!")

@blog_bp.route("/blog/7-different-types-of-porcelain-tiles-explained/")
def blog_inside20():
    return render_template('blog-inside-20.html',title='7 DIFFERENT TYPES OF PORCELAIN TILES EXPLAINED!',desc="Did you know there are many types of porcelain tiles available in the market? Lioli Ceramica explains the seven types of porcelain tiles so that you will know how each different and unique type of tile differs. Read the blog to know more!")

@blog_bp.route("/blog/large-format-porcelain-wall-tile-installation-guide/")
def blog_inside21():
    return render_template('blog-inside-21.html',title='LARGE-FORMAT PORCELAIN WALL TILE INSTALLATION GUIDE',desc="While large format tiles look stunning, their laying can be a bit complicated. In this blog, Lioli Ceramica explains the wall tile installation process, some common mistakes to avoid, and some extra tips to ensure your walls look perfect once you tile them up!")






@blog_bp.route("/blog/glossy-vs-matt-finish-porcelain-tiles/")
def blog_inside22():
    return render_template('blog-inside-22.html',title='Glossy Vs Matt Finish Porcelain Tiles: What Is The Difference?',desc="Glossy and matte finish porcelain tiles are the first choice for many homeowners. You can identify one by the presence of a shiny surface. But there are many more differences between glossy and matte finish tiles than mere shiny appearance. Read on the blog to know more. ")

