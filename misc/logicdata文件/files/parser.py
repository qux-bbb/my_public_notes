# coding:utf8

def to_num(bit_list):
    result = 0
    for i in bit_list[::-1]:
        result = (result << 1) + i
    return result

def main():
    the_file = open('data.csv', 'r')
    the_lines = the_file.readlines()
    the_file.close()

    lastClk = 0
    lastData = 0
    mode = ''
    dataBuf = []
    outCounter = 0
    psc = []

    for line in the_lines:
        if ',' not in line or line.startswith(('Time', '-')):
            continue
        _time, clk, data = line.strip().split(', ')
        clk = int(clk)
        data = int(data)

        dataFall = data < lastData
        dataRise = data > lastData
        clkH = clk > 0

        if mode == '':
            if dataFall and clkH:  # 表示命令模式开始
                mode = 'command'
                dataBuf = []
        elif mode == 'command':
            if dataRise and clkH:  # 表示命令模式结束
                control = to_num(dataBuf[:8])
                address = to_num(dataBuf[8:16])
                data = to_num(dataBuf[16:])
                if control == 0b00110000:
                    outCounter = (256-address)*8+1
                    mode = 'outgoing'
                    command = 'read main memory'
                elif control == 0b00111000:
                    mode = 'processing'
                    command = 'update main memory'
                elif control == 0b00110100:
                    # The command transfers the protection bits under a continuous input of 32 clock pulses to the output.
                    # I/O is switched to high impedance Z by an additional pulse.
                    # 所以是32+1
                    outCounter = 32 + 1
                    mode = 'outgoing'
                    command = 'read protection memory'
                elif control == 0b00111100:
                    mode = 'processing'
                    command = 'write protection memory'
                elif control == 0b00110001:
                    outCounter = 32 + 1
                    mode = 'outgoing'
                    command = 'read security memory'
                elif control == 0b00111001:
                    mode = 'processing'
                    command = 'update security memory'
                elif control == 0b00110011:
                    psc.append(data)
                    mode = 'processing'
                    command = 'compare verification data'
                else:
                    mode = ''
                    command = 'unknown'

                print()
                print('command: {}'.format(command))

                if mode == 'processing':
                    outCounter = 0  # TODO 还没找到这个逻辑
                print('address: {}'.format(address))
                print('data: {}'.format(hex(data)))
            elif clkH:
                dataBuf.append(data)
        elif mode == 'outgoing':
            if clkH:
                dataBuf.append(data)
                outCounter -= 1
                if outCounter <= 0:
                    print('{} bits transferred'.format(len(dataBuf)))
                    mode = ''
        elif mode == 'processing':
            if clkH:
                outCounter += 1  # TODO 还没找到这个逻辑
            if dataRise:
                print('processing for {} cycles'.format(outCounter))
                mode = ''

        lastClk = clk
        lastData = data

    print()
    print('PSC: {:0>2x} {:0>2x} {:0>2x}'.format(psc[0], psc[1], psc[2]))


if __name__ == '__main__':
    main()