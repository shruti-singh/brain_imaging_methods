﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Fri 09 Apr 2021 08:28:43 AM IST
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.3'
expName = 'ldt_en_hi'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/home/shruti/Desktop/iitgn/courses/SEM4/BrainImagingMethods/experiments/brain_imaging_methods/Assignment3/ldt_en_hi_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
eninstrstim = visual.TextBox2(
     win, text='Instructions:\n\nA pair of commonly used english words will be flashed on the screen. \nPress the right arrow key if both the words are valid english words. \nPress the left arrow key if either one of the words or both words are not valid english words.\n\nPress left/right keys to try out few examples.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='eninstrstim',
     autoLog=True,
)
enkbinstr = keyboard.Keyboard()

# Initialize components for Routine "en_warmup"
en_warmupClock = core.Clock()
enwarmupw1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.1,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='enwarmupw1',
     autoLog=True,
)
enwarmupw2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.1,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='bottom-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='enwarmupw2',
     autoLog=True,
)
enwarmupkb = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
restresp = keyboard.Keyboard()

# Initialize components for Routine "startexp"
startexpClock = core.Clock()
startexpprompt = visual.TextBox2(
     win, text='Press left/right arrow key to start the experiment.', font='Open Sans',
     pos=(0, 0),     letterHeight=0.1,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='startexpprompt',
     autoLog=True,
)
startexpkbresp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
en_w1 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.1,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='en_w1',
     autoLog=True,
)
en_w2 = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.1,
     size=None, borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='bottom-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='en_w2',
     autoLog=True,
)
enkbresp = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
restresp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
enkbinstr.keys = []
enkbinstr.rt = []
_enkbinstr_allKeys = []
# keep track of which components have finished
instrComponents = [eninstrstim, enkbinstr]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *eninstrstim* updates
    if eninstrstim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        eninstrstim.frameNStart = frameN  # exact frame index
        eninstrstim.tStart = t  # local t and not account for scr refresh
        eninstrstim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(eninstrstim, 'tStartRefresh')  # time at next scr refresh
        eninstrstim.setAutoDraw(True)
    
    # *enkbinstr* updates
    waitOnFlip = False
    if enkbinstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enkbinstr.frameNStart = frameN  # exact frame index
        enkbinstr.tStart = t  # local t and not account for scr refresh
        enkbinstr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enkbinstr, 'tStartRefresh')  # time at next scr refresh
        enkbinstr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enkbinstr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enkbinstr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enkbinstr.status == STARTED and not waitOnFlip:
        theseKeys = enkbinstr.getKeys(keyList=['left', 'right'], waitRelease=False)
        _enkbinstr_allKeys.extend(theseKeys)
        if len(_enkbinstr_allKeys):
            enkbinstr.keys = _enkbinstr_allKeys[-1].name  # just the last key pressed
            enkbinstr.rt = _enkbinstr_allKeys[-1].rt
            # was this correct?
            if (enkbinstr.keys == str('')) or (enkbinstr.keys == ''):
                enkbinstr.corr = 1
            else:
                enkbinstr.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('eninstrstim.started', eninstrstim.tStartRefresh)
thisExp.addData('eninstrstim.stopped', eninstrstim.tStopRefresh)
# check responses
if enkbinstr.keys in ['', [], None]:  # No response was made
    enkbinstr.keys = None
    # was no response the correct answer?!
    if str('').lower() == 'none':
       enkbinstr.corr = 1;  # correct non-response
    else:
       enkbinstr.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('enkbinstr.keys',enkbinstr.keys)
thisExp.addData('enkbinstr.corr', enkbinstr.corr)
if enkbinstr.keys != None:  # we had a response
    thisExp.addData('enkbinstr.rt', enkbinstr.rt)
thisExp.addData('enkbinstr.started', enkbinstr.tStartRefresh)
thisExp.addData('enkbinstr.stopped', enkbinstr.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
enwarmuptrials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('dataset/en_warmupconditions.csv'),
    seed=None, name='enwarmuptrials')
thisExp.addLoop(enwarmuptrials)  # add the loop to the experiment
thisEnwarmuptrial = enwarmuptrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEnwarmuptrial.rgb)
if thisEnwarmuptrial != None:
    for paramName in thisEnwarmuptrial:
        exec('{} = thisEnwarmuptrial[paramName]'.format(paramName))

for thisEnwarmuptrial in enwarmuptrials:
    currentLoop = enwarmuptrials
    # abbreviate parameter names if possible (e.g. rgb = thisEnwarmuptrial.rgb)
    if thisEnwarmuptrial != None:
        for paramName in thisEnwarmuptrial:
            exec('{} = thisEnwarmuptrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "en_warmup"-------
    continueRoutine = True
    # update component parameters for each repeat
    enwarmupw1.setText(w_word1)
    enwarmupw2.setText(w_word2)
    enwarmupkb.keys = []
    enwarmupkb.rt = []
    _enwarmupkb_allKeys = []
    # keep track of which components have finished
    en_warmupComponents = [enwarmupw1, enwarmupw2, enwarmupkb]
    for thisComponent in en_warmupComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    en_warmupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "en_warmup"-------
    while continueRoutine:
        # get current time
        t = en_warmupClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=en_warmupClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *enwarmupw1* updates
        if enwarmupw1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enwarmupw1.frameNStart = frameN  # exact frame index
            enwarmupw1.tStart = t  # local t and not account for scr refresh
            enwarmupw1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enwarmupw1, 'tStartRefresh')  # time at next scr refresh
            enwarmupw1.setAutoDraw(True)
        if enwarmupw1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enwarmupw1.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                enwarmupw1.tStop = t  # not accounting for scr refresh
                enwarmupw1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enwarmupw1, 'tStopRefresh')  # time at next scr refresh
                enwarmupw1.setAutoDraw(False)
        
        # *enwarmupw2* updates
        if enwarmupw2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enwarmupw2.frameNStart = frameN  # exact frame index
            enwarmupw2.tStart = t  # local t and not account for scr refresh
            enwarmupw2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enwarmupw2, 'tStartRefresh')  # time at next scr refresh
            enwarmupw2.setAutoDraw(True)
        if enwarmupw2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > enwarmupw2.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                enwarmupw2.tStop = t  # not accounting for scr refresh
                enwarmupw2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(enwarmupw2, 'tStopRefresh')  # time at next scr refresh
                enwarmupw2.setAutoDraw(False)
        
        # *enwarmupkb* updates
        waitOnFlip = False
        if enwarmupkb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enwarmupkb.frameNStart = frameN  # exact frame index
            enwarmupkb.tStart = t  # local t and not account for scr refresh
            enwarmupkb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enwarmupkb, 'tStartRefresh')  # time at next scr refresh
            enwarmupkb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enwarmupkb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enwarmupkb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enwarmupkb.status == STARTED and not waitOnFlip:
            theseKeys = enwarmupkb.getKeys(keyList=['left', 'right'], waitRelease=False)
            _enwarmupkb_allKeys.extend(theseKeys)
            if len(_enwarmupkb_allKeys):
                enwarmupkb.keys = _enwarmupkb_allKeys[-1].name  # just the last key pressed
                enwarmupkb.rt = _enwarmupkb_allKeys[-1].rt
                # was this correct?
                if (enwarmupkb.keys == str(w_corrAns)) or (enwarmupkb.keys == w_corrAns):
                    enwarmupkb.corr = 1
                else:
                    enwarmupkb.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in en_warmupComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "en_warmup"-------
    for thisComponent in en_warmupComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    enwarmuptrials.addData('enwarmupw1.started', enwarmupw1.tStartRefresh)
    enwarmuptrials.addData('enwarmupw1.stopped', enwarmupw1.tStopRefresh)
    enwarmuptrials.addData('enwarmupw2.started', enwarmupw2.tStartRefresh)
    enwarmuptrials.addData('enwarmupw2.stopped', enwarmupw2.tStopRefresh)
    # check responses
    if enwarmupkb.keys in ['', [], None]:  # No response was made
        enwarmupkb.keys = None
        # was no response the correct answer?!
        if str(w_corrAns).lower() == 'none':
           enwarmupkb.corr = 1;  # correct non-response
        else:
           enwarmupkb.corr = 0;  # failed to respond (incorrectly)
    # store data for enwarmuptrials (TrialHandler)
    enwarmuptrials.addData('enwarmupkb.keys',enwarmupkb.keys)
    enwarmuptrials.addData('enwarmupkb.corr', enwarmupkb.corr)
    if enwarmupkb.keys != None:  # we had a response
        enwarmuptrials.addData('enwarmupkb.rt', enwarmupkb.rt)
    enwarmuptrials.addData('enwarmupkb.started', enwarmupkb.tStartRefresh)
    enwarmuptrials.addData('enwarmupkb.stopped', enwarmupkb.tStopRefresh)
    # the Routine "en_warmup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    restresp.keys = []
    restresp.rt = []
    _restresp_allKeys = []
    # keep track of which components have finished
    restComponents = [restresp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *restresp* updates
        waitOnFlip = False
        if restresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            restresp.frameNStart = frameN  # exact frame index
            restresp.tStart = t  # local t and not account for scr refresh
            restresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restresp, 'tStartRefresh')  # time at next scr refresh
            restresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(restresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(restresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if restresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restresp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                restresp.tStop = t  # not accounting for scr refresh
                restresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restresp, 'tStopRefresh')  # time at next scr refresh
                restresp.status = FINISHED
        if restresp.status == STARTED and not waitOnFlip:
            theseKeys = restresp.getKeys(keyList=None, waitRelease=False)
            _restresp_allKeys.extend(theseKeys)
            if len(_restresp_allKeys):
                restresp.keys = _restresp_allKeys[-1].name  # just the last key pressed
                restresp.rt = _restresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if restresp.keys in ['', [], None]:  # No response was made
        restresp.keys = None
    enwarmuptrials.addData('restresp.keys',restresp.keys)
    if restresp.keys != None:  # we had a response
        enwarmuptrials.addData('restresp.rt', restresp.rt)
    enwarmuptrials.addData('restresp.started', restresp.tStartRefresh)
    enwarmuptrials.addData('restresp.stopped', restresp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'enwarmuptrials'


# ------Prepare to start Routine "startexp"-------
continueRoutine = True
# update component parameters for each repeat
startexpkbresp.keys = []
startexpkbresp.rt = []
_startexpkbresp_allKeys = []
# keep track of which components have finished
startexpComponents = [startexpprompt, startexpkbresp]
for thisComponent in startexpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startexpClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startexp"-------
while continueRoutine:
    # get current time
    t = startexpClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startexpClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *startexpprompt* updates
    if startexpprompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startexpprompt.frameNStart = frameN  # exact frame index
        startexpprompt.tStart = t  # local t and not account for scr refresh
        startexpprompt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startexpprompt, 'tStartRefresh')  # time at next scr refresh
        startexpprompt.setAutoDraw(True)
    
    # *startexpkbresp* updates
    waitOnFlip = False
    if startexpkbresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startexpkbresp.frameNStart = frameN  # exact frame index
        startexpkbresp.tStart = t  # local t and not account for scr refresh
        startexpkbresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startexpkbresp, 'tStartRefresh')  # time at next scr refresh
        startexpkbresp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startexpkbresp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startexpkbresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startexpkbresp.status == STARTED and not waitOnFlip:
        theseKeys = startexpkbresp.getKeys(keyList=['left', 'right'], waitRelease=False)
        _startexpkbresp_allKeys.extend(theseKeys)
        if len(_startexpkbresp_allKeys):
            startexpkbresp.keys = _startexpkbresp_allKeys[-1].name  # just the last key pressed
            startexpkbresp.rt = _startexpkbresp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startexpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startexp"-------
for thisComponent in startexpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('startexpprompt.started', startexpprompt.tStartRefresh)
thisExp.addData('startexpprompt.stopped', startexpprompt.tStopRefresh)
# check responses
if startexpkbresp.keys in ['', [], None]:  # No response was made
    startexpkbresp.keys = None
thisExp.addData('startexpkbresp.keys',startexpkbresp.keys)
if startexpkbresp.keys != None:  # we had a response
    thisExp.addData('startexpkbresp.rt', startexpkbresp.rt)
thisExp.addData('startexpkbresp.started', startexpkbresp.tStartRefresh)
thisExp.addData('startexpkbresp.stopped', startexpkbresp.tStopRefresh)
thisExp.nextEntry()
# the Routine "startexp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
en_trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='en_trials')
thisExp.addLoop(en_trials)  # add the loop to the experiment
thisEn_trial = en_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEn_trial.rgb)
if thisEn_trial != None:
    for paramName in thisEn_trial:
        exec('{} = thisEn_trial[paramName]'.format(paramName))

for thisEn_trial in en_trials:
    currentLoop = en_trials
    # abbreviate parameter names if possible (e.g. rgb = thisEn_trial.rgb)
    if thisEn_trial != None:
        for paramName in thisEn_trial:
            exec('{} = thisEn_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    en_w1.setText(word1)
    en_w2.setText(word2)
    enkbresp.keys = []
    enkbresp.rt = []
    _enkbresp_allKeys = []
    # keep track of which components have finished
    trialComponents = [en_w1, en_w2, enkbresp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *en_w1* updates
        if en_w1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            en_w1.frameNStart = frameN  # exact frame index
            en_w1.tStart = t  # local t and not account for scr refresh
            en_w1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(en_w1, 'tStartRefresh')  # time at next scr refresh
            en_w1.setAutoDraw(True)
        
        # *en_w2* updates
        if en_w2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            en_w2.frameNStart = frameN  # exact frame index
            en_w2.tStart = t  # local t and not account for scr refresh
            en_w2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(en_w2, 'tStartRefresh')  # time at next scr refresh
            en_w2.setAutoDraw(True)
        
        # *enkbresp* updates
        waitOnFlip = False
        if enkbresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enkbresp.frameNStart = frameN  # exact frame index
            enkbresp.tStart = t  # local t and not account for scr refresh
            enkbresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enkbresp, 'tStartRefresh')  # time at next scr refresh
            enkbresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enkbresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enkbresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enkbresp.status == STARTED and not waitOnFlip:
            theseKeys = enkbresp.getKeys(keyList=['left', 'right'], waitRelease=False)
            _enkbresp_allKeys.extend(theseKeys)
            if len(_enkbresp_allKeys):
                enkbresp.keys = _enkbresp_allKeys[-1].name  # just the last key pressed
                enkbresp.rt = _enkbresp_allKeys[-1].rt
                # was this correct?
                if (enkbresp.keys == str(corrAns)) or (enkbresp.keys == corrAns):
                    enkbresp.corr = 1
                else:
                    enkbresp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    en_trials.addData('en_w1.started', en_w1.tStartRefresh)
    en_trials.addData('en_w1.stopped', en_w1.tStopRefresh)
    en_trials.addData('en_w2.started', en_w2.tStartRefresh)
    en_trials.addData('en_w2.stopped', en_w2.tStopRefresh)
    # check responses
    if enkbresp.keys in ['', [], None]:  # No response was made
        enkbresp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           enkbresp.corr = 1;  # correct non-response
        else:
           enkbresp.corr = 0;  # failed to respond (incorrectly)
    # store data for en_trials (TrialHandler)
    en_trials.addData('enkbresp.keys',enkbresp.keys)
    en_trials.addData('enkbresp.corr', enkbresp.corr)
    if enkbresp.keys != None:  # we had a response
        en_trials.addData('enkbresp.rt', enkbresp.rt)
    en_trials.addData('enkbresp.started', enkbresp.tStartRefresh)
    en_trials.addData('enkbresp.stopped', enkbresp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    restresp.keys = []
    restresp.rt = []
    _restresp_allKeys = []
    # keep track of which components have finished
    restComponents = [restresp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *restresp* updates
        waitOnFlip = False
        if restresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            restresp.frameNStart = frameN  # exact frame index
            restresp.tStart = t  # local t and not account for scr refresh
            restresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(restresp, 'tStartRefresh')  # time at next scr refresh
            restresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(restresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(restresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if restresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > restresp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                restresp.tStop = t  # not accounting for scr refresh
                restresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(restresp, 'tStopRefresh')  # time at next scr refresh
                restresp.status = FINISHED
        if restresp.status == STARTED and not waitOnFlip:
            theseKeys = restresp.getKeys(keyList=None, waitRelease=False)
            _restresp_allKeys.extend(theseKeys)
            if len(_restresp_allKeys):
                restresp.keys = _restresp_allKeys[-1].name  # just the last key pressed
                restresp.rt = _restresp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if restresp.keys in ['', [], None]:  # No response was made
        restresp.keys = None
    en_trials.addData('restresp.keys',restresp.keys)
    if restresp.keys != None:  # we had a response
        en_trials.addData('restresp.rt', restresp.rt)
    en_trials.addData('restresp.started', restresp.tStartRefresh)
    en_trials.addData('restresp.stopped', restresp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'en_trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
