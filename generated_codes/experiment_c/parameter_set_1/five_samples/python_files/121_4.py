

A:

You can solve this problem in O(n) time complexity and O(1) space complexity.

Take the input
Keep two pointers, left and right and set them at 0 and n respectively
Take two counters, left_counter and right_counter and set them at 1 and 1 respectively
Iterate until left <= right
a) Add the left_counter and right_counter to the total distance and increment them by 1
b) If left_counter is even, left +=1; else right -=1

The code would look something like this.
<code>def lights_off_distance(n):
    left = 0; right = n; distance = 0; right_counter = 1; left_counter = 1
    while(left &lt;= right):
        distance += (left_counter + right_counter)
        left_counter += 1
        right_counter += 1
        if(left_counter%2 == 0):
            left += 1
        else:
            right -= 1
    return distance

print(lights_off_distance(10))
</code>
You can change the input in the function to test it.
