# 개요

첨부된 파일은 노이즈와 모션블러에 의해서 훼손된 영상이다.

[1] cameraman_gaussian_noise.png : Gaussian noise만 있는 영상

[2] cameraman_sp_noise.png: Salt&Pepper noise만 있는 영상

[3] cameraman_motion_blurred.png: Motion blur에 의해 degradation된 영상

노이즈를 제거하기 위해서 [1] [2] 영상에 대해서 adaptive mean filtering, adaptive median filtering을 각각 적용하여 노이즈를 제거한 결과를 구하고,

열화된 영상을 복원하기 위해서 [3] 영상에 대해서 least square error filter (Wiener filter)를 적용하여 그 결과를 구하라.

제출물은 보고서와, 보고서에 결과로 사용한 복원된 결과 영상 파일이다.

[첨가:2020-05-30] 과제에 대해서 질문이 있어서 답변을 과제에 대한 재 설명으로 갈음합니다.

첨부한 파일 [1][2]는 노이즈의 양상이 다릅니다. 다른 노이즈 양상에 대해서 adaptive mean/median filters가 어떻게 다른 결과를 내는지를 검증해 보기 위해서 두 영상에 각각 두개의 필터를 적용해서 결과를 비교하면, 특정 노이즈 패턴에 두 필터 중에서 어느쪽이 우월한지, 혹은 노이즈 패턴에 상관없이 어느 한쪽 필터가 항상 우월한지를 검증해 볼 수 있을 것 입니다. 첨부 파일 [3]은 노이즈가 전혀 없는 모션블러만 있는 그림인데, 블러의 방향과 양이 알려져 있지 않은데 그런 경우에도 wiener filter가 잘 작동하는지를 검토해 보자는 뜻 입니다.

따라서 [1]에 adaptive mean filter와 adaptive median filter를 적용한 결과와 비교, [2]에 adaptive mean filter와 adaptive median filter를 적용한 결과와 비교, 그에 따라서 노이즈로부터 복원하는 두 필터의 우월성 비교가 필요하고, [3]에 wiener filter를 적용하여 어떤 SNR (정확히는 NSR이죠)에서 좋은 결과로 복원이 되는지를 확인하면 됩니다.

/Users/yongsangho/Desktop/git/Digital-Image-Processing/cameraman_motion_blurred.png
![original](./Digital-Image-Processing/cameraman_motion_blurred.png)
/Users/yongsangho/Desktop/git/Digital-Image-Processing/cameraman_sp_noise.png


/Users/yongsangho/Desktop/git/Digital-Image-Processing/cameraman_gaussian_noise.png
<Cameraman_motion_blurred.png> <Cameraman_sp_noise.png>   <Cameraman_Gaussian_noise.png>
