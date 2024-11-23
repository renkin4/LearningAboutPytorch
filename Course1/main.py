import torch 
print(torch.__version__)


#TENSOR 
TENSOR = torch.tensor([[[1,2,3], [3,6,8], [2,4,5]]])

print(TENSOR)

print(TENSOR.ndim)
print(TENSOR.shape)