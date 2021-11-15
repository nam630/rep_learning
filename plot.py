import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main():
    filenames = ['default_CURL_4000MC_400E', 'pixels_rew', 'resnet_encoder_rew', 'vgg_encoder_rew']
    labels = ['curl', 'pixel', 'resnet', 'vgg']
    for (i, f) in enumerate(filenames):
        if i > 0:
            rew = np.load(f + '.npy')
            print(len(rew))
            rew = pd.DataFrame(rew).rolling(window=20).mean()
            plt.plot(rew, label=labels[i])
    plt.legend()
    plt.xlabel('train episode')
    plt.ylabel('rewards')
    plt.title('Train episodes v.s. rewards')
    plt.savefig('learning_curve_shorter.png')

if __name__ == "__main__":
    main()
