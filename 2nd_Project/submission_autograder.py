# submission_autograder.py
# ------------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


#!/usr/bin/env python
# -*- coding: utf-8 -*-


from codecs import open

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))

