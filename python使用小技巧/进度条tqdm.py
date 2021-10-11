from tqdm import tqdm
import time

loader = [[chr(i),i] for i in range(97,97+26)]
bar = tqdm(enumerate(loader),total=len(loader),colour='green')

for idx,char in bar:
    time.sleep(0.05)
    bar.set_description("Processing %s" % char[0])