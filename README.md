# BitPy

A BitTorrent client

A BitTorrent client in Python 3.5

Python 3.5 comes with support for asynchronous IO, which seems like a perfect fit when implementing a BitTorrent client. This article will guide you through the BitTorrent protocol details while showcasing how a small client was implemented using it.
Wednesday, August 24, 2016

When Python 3.5 was released together with the new module asyncio I was curios to give it a try. Recently I decided to implement a simple BitTorrent client using asyncio - I have always been interested in peer-to-peer protocols and it seemed like a perfect fit.

The project is named Pieces, all of the source code is available at GitHub and released under the Apache 2 license. Feel free to learn from it, steal from it, improve it, laugh at it or just ignore it.

I previously posted a short introduction to Python’s async module. If this is your first time looking at asyncio it might be a good idea to read through that one first.
