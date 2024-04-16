# All different evaluations are stored in this directory

## Note that although there are a lot of files in this directory, most of them do very similar functions and share very similar layouts.

### Redraw and evaluationNavigator are the only two that differ to a decent degree.

## Possible Dimensions:

1. alignment
2. bisection
3. bisectionAngle
4. closure
5. equilaterality
6. lineRatio
7. roundness
8. spacing
9. straightness

<br><br>

# Each measure specified dimensions

## - **Circle:** closure, round

## - **DoubleLine:** alignment, equilaterality, straightness

## - **MiniVerticalLines:** alignment, equilaterality, straightness

## - **PlusSign:** bisection, bisectionAngle, straightness

## - **SingleLine:** straightness

## - **Square:** closure, equilaterality, straightness

## - **Triangle:** closure, equilaterality, straightness

## - **TripleLine:** alignment, equilaterality, lineRatio, spacing, straightness

## - **VerticalLine:** straightness

<br><br>

# evaluationNavigator.js

## This is responsible for sending data to/from the back-end when taking tests.

## It is also responsible for the order in which tests are taken.

### The exception to this is Instructions.js - it determines which goes first. (Instructions.js is not in this directory.)

## Note that evaluationNavigator is _NOT_ a component; just a few functions that are resused.

<br><br>

# Redraw.js

## Redraw is responsible for redrawing whatever was selected on the record page.

### It is in this directory because its functionality is very similar to all of the other components for drawing shapes.
