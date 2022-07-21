import numpy as np
import scanpy as sc
import pandas as pd
adult_wc_path = '../../results/logs1/adult_wc_T.csv'
adult_wc = sc.read_csv(adult_wc_path)
# adult_wc.write_csvs('../results/adult_wc/')
sc.pp.neighbors(adult_wc, n_neighbors=10, n_pcs=40)
sc.tl.umap(adult_wc)
sc.tl.tsne(adult_wc)
# sc.pl.umap(adult_wc,color='mt.Rnr2')
sc.tl.leiden(adult_wc)
sc.pl.umap(adult_wc, color=['leiden'])
sc.pl.tsne(adult_wc, color=['leiden'])