def parse_molecule(f):
    atoms = {}
    for i in range(len(f)):
        if f[i].isupper():
            if i == len(f) - 1:
                c = 1
                a = f[i]
            else:
                step = 2 if f[i+1].islower() and i < len(f) - 2 else 1
                if not f[i+step].isdigit():
                    c = 1
                else:
                    c, deci = 0, 1
                    while f[i+step].isdigit():
                        c *= deci
                        c += int(f[i+step])
                        step += 1
                        deci *= 10
                        if i + step == len(f):
                            break
                a = f[i] + f[i+1] if f[i+1].islower() else f[i]
            open_par = len([k for k in f[:i] if k in ['(', '[', '{']]) - len([j for j in f[:i] if j in [')', ']', '}']])
            multi, count_, find_, skipper = 1, 1, 0, 0
            while find_ < open_par:
                if f[i+count_] in ['(', '[', '{']:
                    skipper += 1
                elif f[i+count_] in [')', ']', '}']: 
                    if skipper:
                        skipper -= 1
                    else:
                        step, num = 1, ''
                        while f[i+count_+step].isdigit():
                            num = f[i+count_+step] +num
                            step += 1
                            if i + count_ + step == len(f):
                                break
                        num = 1 if not num else int(num)
                        multi *= num
                        find_ += 1
                count_ += 1
            atoms[a] = c * multi + atoms[a] if a in atoms else c *multi
    return atoms




print(parse_molecule('Pd[P(C6H5)3]4'))

