

A:

The general rule is:
<blockquote>
<p>The number of pieces has to be divisible by <code>&lt;code&gt;n&lt;/code&gt;</code> if you want to have <code>&lt;code&gt;n&lt;/code&gt;</code> equal pieces.</p>
</blockquote>
The only exception is the case when the number of pieces is 2.
<code>def answer(n):
    if n == 2:
        return "y y y"
    elif n % 2 == 0:
        return "y y n"
    return "n y n"

print(answer(4))
print(answer(7))
</code>
