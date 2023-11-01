# python3

import idautils
import idc


def is_immediate_operand(ea, n):
    """检查指定地址和操作数索引的操作数是否为立即数"""
    return idc.get_operand_type(ea, n) == idc.o_imm


DEBUG_FLAG = False
func_ea = 0x030A3170  # 替换为你的函数地址
max_args = 2  # 设置你希望获取的最大参数数量

print("开始搜索函数调用及其参数...")

found = False  # 标记是否找到了目标函数的调用

# 遍历所有到目标函数的交叉引用
for xref in idautils.XrefsTo(func_ea):
    found = True
    caller_ea = xref.frm
    args = []

    # 从call指令往前找push指令
    inst_ea = caller_ea
    while True:
        inst_ea = idc.prev_head(inst_ea)
        mnem = idc.print_insn_mnem(inst_ea)
        if mnem == "push":
            if is_immediate_operand(inst_ea, 0):
                operand = idc.get_operand_value(inst_ea, 0)
                args.append(operand)  # 添加到参数列表

                if len(args) >= max_args:  # 检查是否已经获取了足够的参数
                    break
            else:
                if DEBUG_FLAG:
                    print(f"非立即数操作数在地址 {hex(inst_ea)} 被跳过")

        elif mnem == "call":  # 如果遇到另一个call指令，停止搜索
            break
        if inst_ea <= caller_ea - 0x100:  # 设置搜索的最大范围，以避免无限循环
            break

    # 使用你提供的输出格式
    if len(args) >= max_args:
        args_str = f"({hex(args[0])}"
        for arg in args[1:]:
            args_str += f", {hex(arg)}"
        args_str += ")"
        print(f"调用函数的地址和参数: {hex(caller_ea)}: {args_str},")
    else:
        if DEBUG_FLAG:
            print(f"调用函数的地址: {hex(caller_ea)} 未找到足够的参数")

if not found:
    print("没有找到目标函数的调用")

print("搜索结束。")

"""
开始搜索函数调用及其参数...
调用函数的地址和参数: 0x309129b: (0x8, 0x3a5687),
调用函数的地址和参数: 0x30912c7: (0x0, 0xfda8b77),
调用函数的地址和参数: 0x30913f3: (0x0, 0x6aa0e84),
调用函数的地址和参数: 0x3091465: (0x0, 0xfed02a7),
调用函数的地址和参数: 0x3091482: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309167b: (0x0, 0x44f8007),
调用函数的地址和参数: 0x3091797: (0x13, 0x5b4d601),
调用函数的地址和参数: 0x30917e3: (0x13, 0xae775e1),
调用函数的地址和参数: 0x309187e: (0x0, 0xd641d17),
调用函数的地址和参数: 0x309192e: (0x0, 0xe48e148),
调用函数的地址和参数: 0x3091b6e: (0x0, 0x79eae4),
调用函数的地址和参数: 0x3091c6f: (0x0, 0xb86de55),
调用函数的地址和参数: 0x3091cac: (0x0, 0x7f96c13),
调用函数的地址和参数: 0x3091de8: (0x0, 0x7f96c13),
调用函数的地址和参数: 0x3091e33: (0x0, 0x7f96c13),
调用函数的地址和参数: 0x3091e51: (0x0, 0x7f96c13),
调用函数的地址和参数: 0x3091e81: (0x0, 0x7a2bc0),
调用函数的地址和参数: 0x3091eb2: (0x0, 0x79eae4),
调用函数的地址和参数: 0x30921a9: (0x9, 0xabc78f7),
调用函数的地址和参数: 0x30921ef: (0x9, 0x8a8238c),
调用函数的地址和参数: 0x3092219: (0x9, 0x90ec817),
调用函数的地址和参数: 0x309233a: (0x0, 0xd6c4b47),
调用函数的地址和参数: 0x309236f: (0x0, 0xfed02a7),
调用函数的地址和参数: 0x30923a7: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30923cd: (0x0, 0x13b274),
调用函数的地址和参数: 0x309264c: (0x0, 0xbf8ba27),
调用函数的地址和参数: 0x309267d: (0x0, 0xc96d047),
调用函数的地址和参数: 0x3092d9f: (0x0, 0xa0733d4),
调用函数的地址和参数: 0x30930ca: (0x14, 0xd926bdb),
调用函数的地址和参数: 0x30931a5: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30931b9: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30931d6: (0x14, 0xc3b09db),
调用函数的地址和参数: 0x3093528: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x30935b3: (0x0, 0x56fde3),
调用函数的地址和参数: 0x3093666: (0x3, 0x87bd287),
调用函数的地址和参数: 0x30936c2: (0xd, 0xdc7cc33),
调用函数的地址和参数: 0x309371d: (0xd, 0x4da8f17),
调用函数的地址和参数: 0x3093747: (0xd, 0xa8b0327),
调用函数的地址和参数: 0x3093cc3: (0x0, 0xb1fd105),
调用函数的地址和参数: 0x3093dd5: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x30943fa: (0x0, 0x79eae4),
调用函数的地址和参数: 0x309442f: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x309445d: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x3094498: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x30944c6: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x3094529: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x309455b: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x30945c2: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x30945ff: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x309463e: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x30948f1: (0x6, 0xd0fb754),
调用函数的地址和参数: 0x3094cc5: (0x3, 0x8a42e41),
调用函数的地址和参数: 0x3094fdb: (0x0, 0x44f8011),
调用函数的地址和参数: 0x30957ae: (0x3, 0x7f28f77),
调用函数的地址和参数: 0x3095856: (0x1, 0x868a4c3),
调用函数的地址和参数: 0x3095897: (0x1, 0x868a4c3),
调用函数的地址和参数: 0x30958c2: (0x1, 0xbc2bff7),
调用函数的地址和参数: 0x30958f5: (0x1, 0x66fa595),
调用函数的地址和参数: 0x3095c81: (0x0, 0x44f8007),
调用函数的地址和参数: 0x3095daa: (0x0, 0xae63487),
调用函数的地址和参数: 0x3095dd7: (0x0, 0x2a85667),
调用函数的地址和参数: 0x3095ea3: (0x0, 0xad68947),
调用函数的地址和参数: 0x3095ed6: (0x0, 0x4166e5),
调用函数的地址和参数: 0x3096160: (0x0, 0xc702be2),
调用函数的地址和参数: 0x3096178: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x3096240: (0x0, 0x3087237),
调用函数的地址和参数: 0x30962cc: (0x0, 0xa39ecc7),
调用函数的地址和参数: 0x3096309: (0x1, 0xf3c7b77),
调用函数的地址和参数: 0x30964be: (0x0, 0x54bca37),
调用函数的地址和参数: 0x309658c: (0x6, 0x69044),
调用函数的地址和参数: 0x3096786: (0x0, 0xd733213),
调用函数的地址和参数: 0x3096815: (0x13, 0xbeb9491),
调用函数的地址和参数: 0x30968a3: (0x13, 0x85dc001),
调用函数的地址和参数: 0x30968fa: (0x13, 0xb157a91),
调用函数的地址和参数: 0x3096ada: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x3096b36: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x3096bcf: (0x0, 0xcaccdc4),
调用函数的地址和参数: 0x3096c07: (0x0, 0xcaccdc4),
调用函数的地址和参数: 0x3096d0c: (0x0, 0xc702be2),
调用函数的地址和参数: 0x3096daa: (0x0, 0xcaccdc4),
调用函数的地址和参数: 0x30970a2: (0x0, 0xcaccdc4),
调用函数的地址和参数: 0x30970b9: (0x0, 0x79eae4),
调用函数的地址和参数: 0x30970dd: (0x0, 0xc702be2),
调用函数的地址和参数: 0x309711d: (0x0, 0xcab48c4),
调用函数的地址和参数: 0x3097134: (0x0, 0xcab48c4),
调用函数的地址和参数: 0x309714b: (0x0, 0xcaccdc4),
调用函数的地址和参数: 0x30973ec: (0x0, 0x6f6e3c7),
调用函数的地址和参数: 0x3097457: (0x0, 0x44f8007),
调用函数的地址和参数: 0x3097843: (0x0, 0xee41457),
调用函数的地址和参数: 0x3097863: (0x0, 0x79eae4),
调用函数的地址和参数: 0x3097881: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30979a4: (0x1, 0xd3997b7),
调用函数的地址和参数: 0x3097a6a: (0x9, 0xbd557e),
调用函数的地址和参数: 0x3097bb3: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x3097bf8: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x3097c2c: (0x0, 0x56fde3),
调用函数的地址和参数: 0x3097caa: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x3097dd1: (0x1, 0xa7d67a7),
调用函数的地址和参数: 0x3097de6: (0x1, 0xcc4b6f7),
调用函数的地址和参数: 0x3097e1a: (0x1, 0xa255257),
调用函数的地址和参数: 0x3097e7f: (0x0, 0xab8ba27),
调用函数的地址和参数: 0x3097eea: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x3097efc: (0x0, 0xad64007),
调用函数的地址和参数: 0x3097f27: (0x0, 0xa0733d4),
调用函数的地址和参数: 0x3098118: (0x9, 0x4a9139c),
调用函数的地址和参数: 0x3098161: (0x9, 0xabc78f7),
调用函数的地址和参数: 0x30981f3: (0x9, 0x8a8238c),
调用函数的地址和参数: 0x3098217: (0x9, 0x4a8239c),
调用函数的地址和参数: 0x30982df: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x309835c: (0x6, 0x79c44),
调用函数的地址和参数: 0x309839f: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x309843f: (0x0, 0xa0733d4),
调用函数的地址和参数: 0x30984a7: (0x0, 0x7a2bc0),
调用函数的地址和参数: 0x30984da: (0x0, 0x6aa0e84),
调用函数的地址和参数: 0x3098537: (0x0, 0xfed02a7),
调用函数的地址和参数: 0x3098862: (0x13, 0x5b4d601),
调用函数的地址和参数: 0x30988a9: (0x0, 0x6ce7d95),
调用函数的地址和参数: 0x3098b6d: (0x0, 0x1e16077),
调用函数的地址和参数: 0x3098bd5: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x3098c0a: (0x9, 0xf2b7ebe),
调用函数的地址和参数: 0x3098c7a: (0x0, 0xc702be2),
调用函数的地址和参数: 0x3098d5c: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30993f0: (0x9, 0xbe1ef6e),
调用函数的地址和参数: 0x3099401: (0x0, 0x160d384),
调用函数的地址和参数: 0x3099421: (0x9, 0xf2b7ebe),
调用函数的地址和参数: 0x3099462: (0x9, 0xa2414e7),
调用函数的地址和参数: 0x30994a6: (0x0, 0xc702be2),
调用函数的地址和参数: 0x30995ef: (0x13, 0x714b685),
调用函数的地址和参数: 0x3099634: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x3099759: (0x0, 0xcb9b43e),
调用函数的地址和参数: 0x30997c9: (0x0, 0x29985de),
调用函数的地址和参数: 0x3099957: (0x0, 0x29985de),
调用函数的地址和参数: 0x3099b84: (0x6, 0xd707572),
调用函数的地址和参数: 0x3099bcd: (0x6, 0x9805d4c),
调用函数的地址和参数: 0x3099c18: (0x6, 0xd0fb754),
调用函数的地址和参数: 0x309a57f: (0x0, 0x8adf2d1),
调用函数的地址和参数: 0x309a5e6: (0x0, 0xb1c1fe3),
调用函数的地址和参数: 0x309a770: (0x0, 0x6aa0e84),
调用函数的地址和参数: 0x309a7f4: (0x0, 0xc8c784),
调用函数的地址和参数: 0x309a893: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x309a8ce: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309a8f9: (0x0, 0x56fde3),
调用函数的地址和参数: 0x309ab96: (0x9, 0xda29a27),
调用函数的地址和参数: 0x309abf5: (0x9, 0x3111c69),
调用函数的地址和参数: 0x309b0c3: (0x0, 0x6aa0e84),
调用函数的地址和参数: 0x309b0ef: (0x0, 0xd6c4b47),
调用函数的地址和参数: 0x309b11f: (0x0, 0xfed02a7),
调用函数的地址和参数: 0x309b13a: (0x0, 0x803f0f3),
调用函数的地址和参数: 0x309b158: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309b210: (0x3, 0xd0682f7),
调用函数的地址和参数: 0x309b222: (0x3, 0x42c2f97),
调用函数的地址和参数: 0x309b63c: (0x0, 0x1f8cae3),
调用函数的地址和参数: 0x309b826: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309b87a: (0x0, 0xec06465),
调用函数的地址和参数: 0x309b8e1: (0x9, 0xf2b7ebe),
调用函数的地址和参数: 0x309b94e: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309ba03: (0x0, 0x6aa0e84),
调用函数的地址和参数: 0x309ba2f: (0x0, 0xd6c4b47),
调用函数的地址和参数: 0x309ba65: (0x0, 0xfed02a7),
调用函数的地址和参数: 0x309ba86: (0x0, 0x803f0f3),
调用函数的地址和参数: 0x309baa4: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309c09c: (0x0, 0x1f8cae3),
调用函数的地址和参数: 0x309c302: (0x0, 0x61f98a7),
调用函数的地址和参数: 0x309c953: (0x6, 0xad54ebf),
调用函数的地址和参数: 0x309c9da: (0x6, 0xc605fbf),
调用函数的地址和参数: 0x309cc65: (0x0, 0x79eae4),
调用函数的地址和参数: 0x309cdec: (0x0, 0xa0733d4),
调用函数的地址和参数: 0x309ce7f: (0x0, 0x79eae4),
调用函数的地址和参数: 0x309d030: (0x13, 0x714b685),
调用函数的地址和参数: 0x309d0fc: (0x13, 0x714b685),
调用函数的地址和参数: 0x309d225: (0x0, 0x79eae4),
调用函数的地址和参数: 0x309d29a: (0x13, 0x714b685),
调用函数的地址和参数: 0x309d458: (0x9, 0x3111c69),
调用函数的地址和参数: 0x309d526: (0x9, 0xda29a27),
调用函数的地址和参数: 0x309d552: (0x9, 0x8097c7),
调用函数的地址和参数: 0x309d57b: (0x9, 0x3111c69),
调用函数的地址和参数: 0x309d616: (0x3, 0x26c10f7),
调用函数的地址和参数: 0x309d670: (0x3, 0x6f3bcc7),
调用函数的地址和参数: 0x309d6b3: (0x0, 0xbf8ba27),
调用函数的地址和参数: 0x309d6e7: (0x0, 0x3087237),
调用函数的地址和参数: 0x309d840: (0x9, 0xda29a27),
调用函数的地址和参数: 0x309d86d: (0x9, 0x8097c7),
调用函数的地址和参数: 0x309d898: (0x9, 0x3111c69),
调用函数的地址和参数: 0x309d8dc: (0x9, 0x8097c7),
调用函数的地址和参数: 0x309d930: (0x0, 0xad68947),
调用函数的地址和参数: 0x309dcc3: (0x1, 0x9c1f217),
调用函数的地址和参数: 0x309dd87: (0x0, 0xbf8ba27),
调用函数的地址和参数: 0x309e208: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309e29e: (0x9, 0xdd270b7),
调用函数的地址和参数: 0x309e337: (0x0, 0x56fde3),
调用函数的地址和参数: 0x309e37f: (0x0, 0xfbf1d65),
调用函数的地址和参数: 0x309e43e: (0x0, 0x78f20f5),
调用函数的地址和参数: 0x309e49c: (0x0, 0xad68947),
调用函数的地址和参数: 0x309e5dd: (0x0, 0xec06465),
调用函数的地址和参数: 0x309e5f8: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309ebd0: (0x0, 0x883cece),
调用函数的地址和参数: 0x309ed40: (0x0, 0x883cece),
调用函数的地址和参数: 0x309f0f3: (0x0, 0x2aa3037),
调用函数的地址和参数: 0x309f1f0: (0x6, 0x7a5a1c4),
调用函数的地址和参数: 0x309f238: (0x6, 0xa654bc4),
调用函数的地址和参数: 0x309f261: (0x6, 0xd707572),
调用函数的地址和参数: 0x309f2d3: (0x0, 0x2aa3037),
调用函数的地址和参数: 0x309f443: (0x0, 0xad68947),
调用函数的地址和参数: 0x309f4f0: (0x0, 0xae63487),
调用函数的地址和参数: 0x309f5a3: (0x0, 0x4aa5b95),
调用函数的地址和参数: 0x309f609: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309f639: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309f6b4: (0x0, 0x16bdb88),
调用函数的地址和参数: 0x309f6ee: (0x0, 0xad68947),
调用函数的地址和参数: 0x309f78c: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x309f7e6: (0x6, 0x86ed427),
调用函数的地址和参数: 0x309f8c0: (0x0, 0xabb2b5),
调用函数的地址和参数: 0x309f8e4: (0x0, 0xc702be2),
调用函数的地址和参数: 0x309f982: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x309fa5f: (0x0, 0xae63487),
调用函数的地址和参数: 0x309fb97: (0x3, 0x1555467),
调用函数的地址和参数: 0x309fc04: (0x0, 0x7a2bc0),
调用函数的地址和参数: 0x309fc7f: (0x0, 0x7a2bc0),
调用函数的地址和参数: 0x309fc9b: (0x0, 0x4aa5b95),
调用函数的地址和参数: 0x309fd20: (0x0, 0xae63487),
调用函数的地址和参数: 0x309fd57: (0x0, 0x2a85667),
调用函数的地址和参数: 0x309feaa: (0x0, 0x4aa5b95),
调用函数的地址和参数: 0x309febc: (0x0, 0xd6756c7),
调用函数的地址和参数: 0x309ff1b: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x309ff40: (0x0, 0xc702be2),
调用函数的地址和参数: 0x309ff65: (0x0, 0xd6fb224),
调用函数的地址和参数: 0x309ff90: (0x0, 0xc702be2),
调用函数的地址和参数: 0x30a00b3: (0x0, 0x2aa3037),
调用函数的地址和参数: 0x30a00f1: (0x0, 0x886d397),
调用函数的地址和参数: 0x30a02fc: (0x6, 0xce53547),
调用函数的地址和参数: 0x30a040c: (0x6, 0xa654bc4),
调用函数的地址和参数: 0x30a0446: (0x6, 0xd0fb754),
调用函数的地址和参数: 0x30a04d0: (0x0, 0x16bdb88),
调用函数的地址和参数: 0x30a04f4: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30a0552: (0x0, 0xb7ac9a5),
调用函数的地址和参数: 0x30a0594: (0x0, 0xb1fd105),
调用函数的地址和参数: 0x30a0606: (0x6, 0xa5f9ac4),
调用函数的地址和参数: 0x30a0647: (0x9, 0x89de501),
调用函数的地址和参数: 0x30a06b4: (0x9, 0x23ed221),
调用函数的地址和参数: 0x30a06d4: (0x9, 0x340868d),
调用函数的地址和参数: 0x30a070b: (0x9, 0xc38858),
调用函数的地址和参数: 0x30a071f: (0x9, 0xcee5ea4),
调用函数的地址和参数: 0x30a07f6: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x30a082c: (0x6, 0x78ba6),
调用函数的地址和参数: 0x30a0846: (0x6, 0xd707572),
调用函数的地址和参数: 0x30a1a49: (0x0, 0xbc487a2),
调用函数的地址和参数: 0x30a2015: (0x3, 0x7f28f61),
调用函数的地址和参数: 0x30a247b: (0x3, 0x7f28f61),
调用函数的地址和参数: 0x30a263a: (0x3, 0x7f28f77),
调用函数的地址和参数: 0x30a3010: (0xc, 0x2360798),
调用函数的地址和参数: 0x30a32be: (0x0, 0xba94474),
调用函数的地址和参数: 0x30a32d3: (0x0, 0xba94474),
调用函数的地址和参数: 0x30a3324: (0xc, 0xc3334a5),
调用函数的地址和参数: 0x30a3943: (0x6, 0xfcab14e),
调用函数的地址和参数: 0x30a3957: (0x6, 0xd0fb754),
调用函数的地址和参数: 0x30a39d5: (0x6, 0x2307572),
调用函数的地址和参数: 0x30a3a03: (0x6, 0x6799c74),
调用函数的地址和参数: 0x30a3b21: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x30a3b53: (0x6, 0x2307572),
调用函数的地址和参数: 0x30a3bee: (0x6, 0x79c2ba4),
调用函数的地址和参数: 0x30a3cbe: (0x6, 0x78ba6),
调用函数的地址和参数: 0x30a3cf2: (0x6, 0x79c44),
调用函数的地址和参数: 0x30a3d83: (0x6, 0xa5f9ac4),
调用函数的地址和参数: 0x30a3da7: (0x6, 0x69044),
调用函数的地址和参数: 0x30a3e01: (0x6, 0xd0fb754),
调用函数的地址和参数: 0x30a3f76: (0x0, 0x56fde3),
调用函数的地址和参数: 0x30a3f95: (0x0, 0xb8e7db5),
调用函数的地址和参数: 0x30a400d: (0x0, 0x79eae4),
调用函数的地址和参数: 0x30a4055: (0x13, 0x7e90205),
调用函数的地址和参数: 0x30a4144: (0x3, 0x8a42e41),
搜索结束。
"""
