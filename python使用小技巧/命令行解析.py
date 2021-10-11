import argparse

parser = argparse.ArgumentParser(description="利用argparse训练网络小demo")
parser.add_argument(
    '--lr',
    type=float,
    default=1e-3,
    # required=True,    # 如果使用该行，则必须要设置lr的值
    help='学习率 (默认: 1e-3)')
parser.add_argument(
    '--resume',
    action='store_true',
    help='是否从提供的检查点恢复训练。 (默认: False)'
)
parser.add_argument(
    '--path_to_checkpoint',
    type=str,
    default='',
    help='恢复检查点的权重路径。 (默认: "")'
)
opt = parser.parse_args()
print(opt)
# python 命令行解析.py --lr=0.11