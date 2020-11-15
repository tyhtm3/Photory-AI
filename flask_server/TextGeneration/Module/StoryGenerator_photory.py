import os
import sys
import random
import torch
import time
from torch.utils.data import DataLoader # 데이터로더
from gluonnlp.data import SentencepieceTokenizer 
from TextGeneration.Module.kogpt2.utils import get_tokenizer
from TextGeneration.Module.kogpt2.utils import download, tokenizer
from TextGeneration.Module.kogpt2.pytorch_kogpt2 import get_pytorch_kogpt2_model
from TextGeneration.Module.model.torch_gpt2 import GPT2Config, GPT2LMHeadModel
from TextGeneration.Module.util.data import NovelDataset
import gluonnlp
import TextGeneration.Module.util.sampling as sampling




class StoryGeneration :
    def __init__(self) :
        ctx= 'cpu'#'cuda' #'cpu' #학습 Device CPU or GPU. colab의 경우 GPU 사용
        cachedir='./kogpt2/model' # KoGPT-2 모델 다운로드 경로
        save_path = 'checkpoints/'
        load_path = 'TextGeneration/Module/checkpoints/narrativeKoGPT2_checkpoint_tokenized_ver3_bat1_epoch350.tar'

        pytorch_kogpt2 = {
            'url': 'https://kobert.blob.core.windows.net/models/kogpt2/pytorch/pytorch_kogpt2_676e9bcfa7.params',
            'fname': 'pytorch_kogpt2_676e9bcfa7.params',
            'chksum': '676e9bcfa7'
        }
        kogpt2_config = {
            "initializer_range": 0.02,
            "layer_norm_epsilon": 1e-05,
            "n_ctx": 1024,
            "n_embd": 768,
            "n_head": 12,
            "n_layer": 12,
            "n_positions": 1024,
            "vocab_size": 50000,
            "activation_function": "gelu"
        }
        
        # download model
        model_info = pytorch_kogpt2
        model_path = download(model_info['url'],
                               model_info['fname'],
                               model_info['chksum'],
                               cachedir=cachedir)
        # download vocab
        vocab_info = tokenizer
        vocab_path = download(vocab_info['url'],
                               vocab_info['fname'],
                               vocab_info['chksum'],
                               cachedir=cachedir)
        
       
        device = torch.device(ctx)
      
        checkpoint = torch.load(load_path, map_location=device)

        # KoGPT-2 언어 모델 학습을 위한 GPT2LMHeadModel 선언
        kogpt2model = GPT2LMHeadModel(config=GPT2Config.from_dict(kogpt2_config))
        kogpt2model.load_state_dict(checkpoint['model_state_dict'])
        kogpt2model.to(device)

        kogpt2model.eval()
        vocab_b_obj = gluonnlp.vocab.BERTVocab.from_sentencepiece(vocab_path,
                                                             mask_token=None,
                                                             sep_token=None,
                                                             cls_token=None,
                                                             unknown_token='<unk>',
                                                             padding_token='<pad>',
                                                             bos_token='<s>',
                                                             eos_token='</s>')
        
        tok_path = get_tokenizer()
        self.model, self.vocab = kogpt2model, vocab_b_obj
        self.tok = SentencepieceTokenizer(tok_path, num_best = 0, alpha=0)
        
        
    def Generate_p_sampling(self, inputText = '') :
        if inputText == '' :
            return '문장을 넣어주세요'
        else :
            sent = inputText

        toked = self.tok(sent)
        #print(toked)
        count = 0
        output_size = 200 # 출력하고자 하는 토큰 갯수
        start = time.time()
       
        while 1:
          input_ids = torch.tensor([self.vocab[self.vocab.bos_token],]  + self.vocab[toked]).unsqueeze(0)
          predicts = self.model(input_ids)
          pred = predicts[0]

          last_pred = pred.squeeze()[-1]
          
          gen = sampling.top_p(last_pred, self.vocab, 0.85)
          

          if count>output_size:
            sent += gen.replace('▁', ' ')
            toked = self.tok(sent)
            count =0
            break
          sent += gen.replace('▁', ' ')
          toked = self.tok(sent)
          count += 1
        
        loc = 0
        sent = sent.replace('</s>', '').replace('<unk>', '')
        conv = False
        for s in range(len(sent)) :
            if conv == False : 
                if sent[s] == "\"" :
                    conv = True
                elif sent[s] =='.' :
                    loc = s
            else :
                if sent[s] == "\"" :
                    conv = False
                    loc = s
            
                
        if loc != 0 :
            sent = sent[:loc+1]
    
        print("time is ", time.time() -  start)
        
        return sent