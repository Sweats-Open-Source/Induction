# Induction.py: Revolutionising Numbers

Integers are overrated. We add them, divide them, multiply them, and subtract
them—and yet, something is always missing.

We blindly assume that integers exist. But what if that assumption is false?
What if writing `4632` tears apart the fine structure of the universe by
introducing a number that has not been proven to exist?

Induction.py solves this problem by inducting numbers into existence, one
import at a time.

The mathematical basis of this is the well-ordering principle applied to the set of positive integers. It states that:
> Every non-empty subset $S$ of $\mathbb{Z}^{+}\$ contains a least element; that is, there exists some $m \in S$ such that $m \leq x$ for every $x \in S$.

## Usage

### Case 1: "I need the number four!"
```python
from induction import one
from one import two
from two import three
from three import four

assert four == one + three
```

### Case 2: "I need the number four thousand, six hundred and thirty-two!"
```python
from induction import one
from one import two
from two import three
from three import four
...
from four_thousand_six_hundred_and_thirty_one import four_thousand_six_hundred_and_thirty_two
```

## Proof

We claim that every positive integer $\(n \in \mathbb{Z}^{+}\)$ can be inducted into existence by this package.

Let

$$
S = \{n \in \mathbb{Z}^{+} : n \text{ cannot be inducted into existence}\}.
$$

Suppose, for contradiction, that \(S\) is non-empty.

By the **Well-Ordering Principle**, every non-empty subset of $\(\mathbb{Z}^{+}\)$ has a least element. Therefore, $\(S\)$ has a least element; call it $\(k\)$.

We first note that

$$
k \neq 1,
$$

because `one` is included explicitly as the base case:

```python
one = 1
make_number(1)
```

Hence,

$$
k > 1.
$$

Therefore,

$$
k-1 \in \mathbb{Z}^{+}.
$$

Since \(k\) is the *least* element of \(S\), \(k-1\notin S\). Thus \(k-1\) can be inducted into existence.

But every inducted number contains the inductive rule

$$
n \longrightarrow n+1.
$$

In particular, once $\(k-1\)$ exists, requesting its successor causes the package to execute

```python
make_number(k)
```

and hence $\(k\)$ is inducted into existence.

This contradicts the assumption that

$$
k \in S.
$$

Therefore $\(S\)$ must be empty.

Hence every positive integer can be inducted into existence:

$$
\boxed{\forall n\in\mathbb{Z}^{+},\; n\text{ is supported by Induction.py}.}
$$

$$
\therefore \text{The natural numbers exist.}
$$

Q.E.D.


## Installation

```bash
pip install num2words
```
## Namespace Rules

`Induction.py` uses the English names produced by `num2words` as module and variable names.

Since Python identifiers cannot contain spaces, hyphens, or commas, number names are normalised according to the following rules:

| Character  | Transformation    |
| ---------- | ----------------- |
| Space ` `  | Replaced with `_` |
| Hyphen `-` | Replaced with `_` |
| Comma `,`  | Removed           |

For example:

```text
twenty-one
→ twenty_one

one hundred and five
→ one_hundred_and_five

one thousand, two hundred
→ one_thousand_two_hundred
```

Therefore, imports follow the normalised form:

```python
from twenty import twenty_one
from one_hundred_and_four import one_hundred_and_five
from one_thousand_one_hundred_and_ninety_nine import one_thousand_two_hundred
```

## Disclaimer

This is a joke. Please do not deploy arithmetic to production. Or do.
