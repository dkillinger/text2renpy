# Text2RenPy
## Introduction
A basic python program that transforms screenplays into Ren'Py game code to promote a better visual novel development workflow.

When developing any Ren'Py game, independent developers are often tasked with juggling their game's narrative alongside their code, sound, and music. While some independent developers eventually find their preferred workflow, the worflow itself is incredibly tedious and draining to many developers. To help these struggling devs, I decided to create _Text2RenPy_ which gives developers the ability to turn already written stories into Ren'Py code. While still in development, I aim to implement the following features:
* Generate all narration/dialogue in the expected Ren'Py syntax.
* Define all Character Objects in a project's "characters.rpy" file.
* Generate all image statements in the expected Ren'Py syntax.
* Define all background/misc images in a project's "images.rpy" file.
* Define all character sprite images in a project's "sprites.rpy" file.
* Generate all audio statements in the expected Ren'Py syntax.
* Define all audio in a project's "audio.rpy" file.
defines character sprite images, generates practical image names, grants the user the ability to control how the resulting code is generated using *Command Statements*, and reports on the resources needed to finish the novel game.

## Important Notes
### Why Screenplays?
Some might be confused as to why screenplays are the only style of writing _currently_ understood by Text2RenPy to produce Ren'Py code, this is because screenplays are very objective compared to more descriptive styles of writing such as novels or poetry. Furthermore, while the formatting is specific, it is not as tedious as writing Ren'Py code manually. Therefore, writing a screenplay allows the developer to focus on their story instead of micromanaging their code.

## Screenplay Format
In respect to Text2RenPy, there are seven main screenplay conventions you must adhere to in order for Text2RenPy to generate the Ren'Py code correctly.
These are:
* Transitions
* Scene Headers
* Actions (interpreted as narration)
* Character Names
* Parentheticals
* Dialogue