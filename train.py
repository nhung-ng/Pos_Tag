# import pickle
# import sklearn_crfsuite
# from sklearn_crfsuite import scorers
# from sklearn_crfsuite import metrics
# import scipy.stats
# from sklearn.metrics import make_scorer
# from sklearn.model_selection import cross_val_score
# from sklearn.model_selection import RandomizedSearchCV

# X_train = open('X_train.pkl', 'rb') 
# X_test = open('X_test.pkl', 'rb') 
# y_train = open('y_train.pkl', 'rb')
# y_test = open('y_test.pkl', 'rb') 
# # try:
#     #X_train = pickle.load(X_train)
# # except:    
#     # X_train.close()
# # try: 
# #     X_test = pickle.load(X_test) 
# # except EOFError: 
# #     X_test.close()
# # try: 
# #     y_train = pickle.load(y_train) 
# # except EOFError: 
# #     y_train.close()
# # try: 
# #     y_test = pickle.load(y_test) 
# # except EOFError: 
# #     y_test.close()                       
# # X_train.close() 
# # X_test.close()
# # y_train.close() 
# # y_test.close() 

# crf = sklearn_crfsuite.CRF(
#     algorithm='lbfgs',
#     max_iterations=100,
#     all_possible_transitions=True
# )
# params_space = {
#     'c1': scipy.stats.expon(scale=0.5),
#     'c2': scipy.stats.expon(scale=0.05),
# }

# # use the same metric for evaluation
# f1_scorer = make_scorer(metrics.flat_f1_score,
#                         average='weighted', labels=crf.classes_)

# # search
# rs = RandomizedSearchCV(crf, params_space,
#                         cv=2,
#                         verbose=1,
#                         n_jobs=12,
#                         n_iter=50,
#                         scoring=f1_scorer)
# rs.fit(X_train, y_train)
# #print('best params:', rs.best_params_)
# #print('best CV score:', rs.best_score_)
# #print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))
# #model = open('tokenizer_model.pkl', 'wb') 
# #pickle.dump(rs.best_estimator_, model, protocol=2)
# #model.close()

