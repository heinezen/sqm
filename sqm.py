#!/usr/bin/env python3

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("base", type=int)
    parser.add_argument("exponent", type=int)
    parser.add_argument("modulus", type=int)

    parser.add_argument("--latex", action='store_true',
                        help='Output LaTeX formatted equations')

    return parser.parse_args()


def startpos(exp: int):
    """
    Get the position of the first bit in the exponent from the right (= least significant
    bit).
    """
    print(f"{exp} = {exp:b}")

    val = 0x01
    pos = 0
    while val < exp:
        val = val << 1
        pos += 1

    pos -= 2

    return pos


def square(cur_val, mod):
    square_val = cur_val ** 2
    mod_square_val = square_val % mod

    print(f"{cur_val}^2 = {square_val} = {mod_square_val} mod {mod}")

    return mod_square_val


def multiply(cur_val, base, mod):
    mul_val = cur_val * base
    mod_mul_val = mul_val % mod

    print(f"{cur_val} * {base} = {mul_val} = {mod_mul_val} mod {mod}")

    return mod_mul_val


def sqm(base: int, exp: int, mod: int):
    """
    Run Square-and-Multiply algorithm.

    :param base: Base value.
    :param exp: Exponent value.
    :param mod: Modulus value.
    """
    cur_val = base % mod
    pos = startpos(exp)

    while pos >= 0:
        cur_val = square(cur_val, mod)

        cur_bit = exp & (0x01 << pos)
        if cur_bit:
            cur_val = multiply(cur_val, base, mod)

        pos -= 1

    print(pow(base, exp, mod))
    print(f"{base}^{exp} = {cur_val} mod {mod}")


def main():
    args = parse_args()

    sqm(args.base, args.exponent, args.modulus)


if __name__ == "__main__":
    main()
