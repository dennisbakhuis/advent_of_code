# Day 14: Parabolic Reflector Dish
So, we've stumbled upon this gigantic parabolic reflector dish attached to a
mountain, right? It's supposed to focus light for energy, but it looks like all
its small mirrors are a bit off, scattering light everywhere instead. There's
this whole setup below it with ropes, pulleys, and a metal platform covered in
rocks of different shapes. Turns out, the way these rocks are arranged on the
platform affects how the dish focuses. The platform can tilt in any direction,
and the round rocks will roll around, while the cube-shaped ones stay put. It
seems like by moving these rocks, we can adjust the dish's focus. Pretty
clever, huh?

## Puzzle 1 - slide stones to the north
We need to tilt the apparatus such that all stones slide to the north. This
will however change the load of the platform and we need to make sure it stays
balanced. I already expect that we need to slide in other directions so lets
implement a generic solution.

## Puzzle 2 - Cycles 
Now we need to rotate the thing in circles. But there is something mean about
it as just brute-forcing the rotations will take forever. We need to find a
cycle pattern and find the last position of the stones.

