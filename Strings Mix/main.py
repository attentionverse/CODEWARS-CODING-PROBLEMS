from string import ascii_lowercase


def mix(s1, s2):
    c1 = [s1.count(ascii_lowercase[i]) for i in range(0, 26)]
    c2 = [s2.count(ascii_lowercase[i]) for i in range(0, 26)]
    m = [max(c1[i], c2[i]) for i in range(0,26)]
    strings = []
    for i in range(0, 26):
        if m[i] > 1:
            prefix = ["2", "1"][m[i] == c1[i]]
            prefix = [prefix, "="][c1[i] == c2[i]]
            strings.append(prefix + ":" + ascii_lowercase[i] * m[i])

    return "/".join(sorted(strings, key = lambda x : (-len(x), x)))


if __name__ == "__main__":
    assert mix("Are they here", "yes, they are here") == "2:eeeee/2:yy/=:hh/=:rr"
    assert mix("looping is fun but dangerous", "less dangerous than coding") == \
        "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg"
    assert mix(" In many languages", " there's a pair of functions") == \
        "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt"
    assert mix("Lords of the Fallen", "gamekult") == "1:ee/1:ll/1:oo"
    assert mix("codewars", "codewars") == ""
    assert mix("A generation must confront the looming ", "codewarrs") == \
        "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"
