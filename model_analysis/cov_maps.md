# Covariance Maps

## SAM 

### Annual

Performance is assessed according to representation of known general characteristics of the SAM, and features of its seasonality, with less weight given to finer details. All CMIP6 models successively represent the broad picture identified in the reanalyses. Over half the models present a highly zonally-symmetric polar region in the mean height field, though a number of others exhibit the more triangular shape, with a particularly prominent protrusion over the Pacific. The three mid-latitude ocean basin highs are also fairly consistently found, although some models have less distinguished maxima and are suggestive of a more summer-dominated pattern, see ACCESS-CM2 for instance. In the HF variance field, the typical annulus structure is generally well represented, approximately centred on the correct latitude and of opposite sign to the mean height field polar region, but with too broad a ring -- the reanalyses has a narrower, more diffuse appearance. HF variance-SAMI covariance in the mid-latitude Pacific is considerable, negative in the western Pacific and negative in the east, whilst ERA-5 sees generally diminished covariance over this region. Maximum covariances in both fields are of comparable magnitude to the reanalyses.

Significant regions are consistently marked where these broad-scale features are found, i.e., the Z500 polar region and surrounding annulus, and the two HF variance annuli. Significance holds less importance in this study, other than to highlight organised co-varying regions. CMCC-CM2-SR5 performs particularly well, with a strong asymmetrical component, and three maxima visible in both fields found collocated with those of ERA-5, however, this asymmetry is retained across all seasons. The CSIRO models fail to capture the asymmetrical component in the mean height field, subsequently possessing a highly symmetrical HF variance ring. The exaggerated ASL region in the FGOALS-f3-L model is again highlighted. The MME mean follows broadly the same picture as the individual models; there are three clear ocean basin maxima, but the mean Z500 polar region is too zonally-symmetric, as is the HF variance ring, and the HF variance covariance over the Pacific is too strong.

### Seasonal

Seasonality of the SAM is reasonably well-represented in most models, capturing the broad themes with variable performance in some of the finer details. Maximum covariances in both fields are comparable to ERA-5 in all seasons, identifying the weakest covariance in autumn and strongest covariance in winter. All models capture the typical summer picture quite well, with most identifying a more symmetrical polar region, though this may be an artefact of the bias toward a symmetrical SAM. There is low covariance over the mid-latitude Pacific in most models (ACCESS-CM2 is unique in having a maximum in this region), in agreement with ERA-5. The HF variance ring is mostly too broad again, though some models perform better than others, such as CESM2-WACCM (Figure?). 

The winter covariance maps exhibit a noticably eccentuated asymmeterical component in both fields for most models, although some still retain a symmetrical polar region. The protruding polar region over the ocean basins are identifiable in many models, with the Pacific protruding arm particularly prominent, as well as a more broken storm track -- all features found in the reanalyses. This wasn't consistent across models however, and the storm track region remains too broad, with spatially continuous regions of strong covariance greater than indicated by ERA-5. Autumn and spring are similarly represented; the overall picture is captured, with marked asymmetry over the polar region, weaker covariance over the Pacific, and a more broken storm track. However, the magnitude of these features is weak relative to the equivalent observed in ERA-5, and many models simulate a much too symmetrical mean height field, and a broad, coherent storm track.

### MME Mean

The MME mean performs well, capturing the typical seasonal cycle -- a symmetrical SAM in summer, much greater asymmetry in winter with a broken storm track region. The zonal displacement of the summertime Z500 maxima over New Zealand and mid-Atlantic toward the Pacific in other seasons is observed in a number a models, and can be seen in the MME mean seasonal maps. Covariance is largest in both fields during winter -- although, the exaggerated difference between winter and summer in ERA-5 HF variance-SAMI covariance is not replicated, and in some models summer possessed the greatest covariance, and may contribute to the more symmetrical SAM -- and weakest in autumn, as per ERA-5. _Note: Interestingly, in spring the ASL region records strong covariance in the mean Z500 field, a notable feature found in the ERA-5 autumn SAM composites -- what does this mean, if anything?_. Covariance is generally lower than the reanalyses and individual models due to the ensemble averaging process and purported independent model realisations.

### Most Accurate Models

CSIRO models eccentuate symmetrical SAM.
CESM2-WACCM does a very good job in summer.
The CMCC-CM2-SR5 model has a summer asymmetrical polar region, which may negate some of the good performance for the annual series. EC-Earth3-CC and EC-Earth3-AerChem perform quite well in summer, despite the weaker performance to date, capturing a symmetrical polar region, weak covariance over the Pacific and diffuse, narrow HF variance annulus.

 - ACCESS-CM2
 - ACCESS-ESM1-5
 - CESM2
 - CESM2-WACCM
 - CMCC-ESM2
 - CMCC-CM2-SR5
 - NorESM2-MM
 - EC-Earth3
 - GFDL-CM4
 - GFDL-ESM4
 - FGOALS-f3-L

## ENSO

### Annual

For the ENSO teleconnection, the broad picture identified in the reanalyses is once again well-represented by most models, see the covariance maps in Figure(?). The negative covariance region over the Amundsen Sea is prominent. Frequently present are the associated positive co-varying regions over the sub-tropical Pacific and the mid-latitude Atlantic. As per the reanalyses, there is a well-aligned region of positive SOI-HF variance covariance in most models, equatorward of the minimum in the mean Z500 field. In the majority of models, this feature was considered signficant according to the FDR method. The extent of this region is more variable, often more or less extensive than ERA-5. Despite clear connections between the two fields, the relationship between mean height covariance and the extent of this region is not obviously linear, as some models have a weaker co-varying mean height field, yet a more extensive HF variance region (see the difference between CESM2 and CMCC-CM2-SR5 in Figure (?) for example). There is a region over Tasmania with positive SOI-HF variance covariance, consistent across the ensemble. This region is observed in the ERA-5 results, but could be construed as coincidental since it was not identified as significant. However, it is interesting to note that it also appears across the CMIP6 ensemble.

Some models have a noticeably weaker performance; CanESM5 fails to identify the ENSO teleconnection in either field, possibly a result of its spectral dynamical core (_I'm not sure why, but this is the one factor that sets it apart from the others, in the weight of its impact results_). HadGEM3-GC31-MM identifies the correct spatial structure, but with particularly weak covariance in the mean Z500 field. MPI-ESM-1-2-HAM exhibits a more circular region over the Amundsen Sea, which may be the cause of the more dispersed SOI-HF variance covariance region over the mid-latitude Pacific. The exaggerated ASL is once again visible in the FGOALS-f3-L covariance map. Maximum covariance was weaker than that found in ERA-5, however, SOI magnitude of the CMIP6 models was approximately half that of ERA-5 due to its derivation, and the associated maximum covariance magnitude is approximately half that of ERA-5 also.

### Seasonal 

Performance capturing ENSO seasonality was weaker than for the SAM, with considerable inter-model variability. All models returned weaker covariance than ERA-5, in line with weaker SOI magnitude, however, this weaker covariance conicides with a generally less organised structure on a hemispheric scale in a number of models. Other features arise with comparable magnitudes to the expected features identified in ERA-5 -- regions of Z500 highs and lows, as well as negatively co-varying regions in the HF variance field. This could indicate a weaker response from the models, failing to adequately capture the scale of the mid-latitude response to ENSO. However, it may be the downscaled SOI means teleconnection features are not well-separated from the variations within the small sample, and so appear more prominently. Some models perform particularly poorly across all seasons, failing to identify the teleconnection in any season. 

In summer, the models largely identify a more SAM-like response in the mean height field, typical of the ENSO teleconnection. However, there is frequently an exaggerated appearance, relative to the background covariance, across the features; the ASL is often more prominent, as is a superposed ZW4 signal, whose maxima are indistinct in the reanalyses (see Figure (?) in chapter 1), whereas they are very clear in some models. The HF variance field also exhibits a SAM-like signal, with a generally broken appearance, representative of the ERA-5 picture. Some models retain too much zonal symmetry, others retain a similar appearance to the annual series, and the occasional model fails to identify the teleconnection signal in one field or the other. CMCC-CM2-SR5 is interesting in its lack of Z500 ASL, but SAM-like HF variance signal (albeit with greater covariance in the opposite hemipshere to the ASL, contrary to ERA-5).

In winter, many models have an identifiable wave train appearance across the Pacific (particularly prominent in NESM3), contrary to ERA-5 results, but in line with previous findings. Almost all models isolate the regional response over the Pacific, as identified in ERA-5 -- a picture largely similar to the annual series with a sub-tropical Pacific positive band, oppositely-signed ASL, with a coherent storm track response equatorward of the ASL. The response in autumn is much more variable across the ensemble, with some identifying a summer-like pattern, others a winter-like pattern, still more with no discernible teleconnection signal at all. This variablility is in line with reduced maximum covariance for autumn compared to other seasons, as in ERA-5, although the difference was relatively small, possibly resulting in a less organised autumnal response. This is not necessarily observed in all models, as some present weaker covariance in winter, at a time when anomalies are usually more extreme. Spring is better represented, with almost all models exhibiting a typical spring teleconnection -- a particularly prominent ASL and associated modified storm track region -- suggesting the improved Rossby wave propagation in spring is well-simulated.

### MME Mean

The annual series structure is true to the reanalyses, with the adjusment for weaker covariance, correctly identifying the sub-tropical Pacific positive band, negative ASL and associated increased equatorward storm track activity, as well as the positive maxima over the Atlantic. The ASL is displaced westward, but the significance of this is unknown. The summer and spring are well-represented, with a highly SAM-like (though perhaps exaggerated) summer teleconnection, and prominent ASL in spring. There is a great reduction in autumn and winter covariance, with minimal structure emerging, whereas ERA-5 results consistently identify the wave train structure over the Pacific.

### Most Accurate Models

CMCC-CM2-SR5 fails to identify the summer Z500 teleconnection signal, does well in the variance field.
CanESM5 is poor is so far off the mark in all seasons.
ACCESS-CM2 does very well in siummer Z500, way too symmetrical in HF variance. 
BCC-CSM2-MR too negative covariance in places.
SAM0-UNICON does a very good job in summer.
HadGEM3-GC31-MM and MPI-ESM-1-2-HAM are poor in winter.

Sample is chosen largely on the basis of successful representation of the phenomena, rather than best in base state, as they are all pretty successful in that regard (although not so much in ST meridional location, should take this into account). 

 - ACCESS-CM2
 - ACCESS-ESM1-5
 - CESM2
 - CESM2-WACCM
 - CMCC-ESM2
 - CMCC-CM2-SR5
 - NorESM2-MM
 - EC-Earth3
 - GFDL-CM4
 - GFDL-ESM4
 - FGOALS-f3-L
 - SAM0-UNICON

## ZW3 

### Annual

A universal clear ZW3 signal is present, with three highs and lows identifiable in the mean Z500 field for most phase bins. Figure (?) provides an ZW3 example for the 120-180 degree phase bin. As per ERA-5, for the majority of models, the strongest extrema are located over the Pacific Ocean. This may be due to the sub-tropical Pacific being a particularly active Rossby wave source, else it could be a consequence emerging from the index derivation noted in chapter 1. Some models have a particularly symmetrical ZW3 signal, CESM2-WACCM has three very clear highs and lows, _I think this is seen somewhere else too_, as does ACCESS-CM2 and NorESM2-MM, whilst others are much weaker outside the Pacific region, see HadGEM3-GC31-MM, GFDL-ESM4 and EC-Earth3-AerChem.

The HF-variance field paints a murkier picture, in line with results from the reanalyses. The nature of the relationship between the mean height and HF variance fields is much less clear for the ZW3 phenomenon, with an array of inconsistent spatial patterns emerging. There is again the general impression, in the annual and seasonal covariance maps, of two regions associated with prominent Z500 extrema -- an equatorward region of the opposite sign, and a poleward region of the same sign. This would appear to be physically sensible; air is deflected clockwise around a low-pressure system, leading to more air directed toward the pole, increasing mean flow velocity hence increased storminess. Whilst air deflected anti-clockwise around a high pressure system would increase equatorward storminess. However, though this may be a component of the overall picture, it doesn't explain the full story, as this pattern is not ubiquitous across covariance maps. The presence of this structure in model output could be a result of model tuning, over-strong physical equations relating to Rossby wave propagation, or weaker internal noise. _Don't like this last sentence, there must be other reasons_. Results for the ensemble mean, shown in Figure (?), provide a similar picture, a well-represented ZW3 Z500 signal, but little consistent repsonse in the HF variance field.

### Seasonal

A ZW3 signal emerges relatively consistently in the mean height field, across the ensemble and across seasons. Any coherent response to ZW3 in the HF variance field remains elusive, but the signal described above appears frequently. Sometimes a ZW4 signal is observed in summer, despite the leading EOFs both possessing ostensible ZW3 signals. Occasionally, three or more of the extrema are missing. Since a ZW3 signal is discernable in the annual series for each model, this is likely a result of the generally weaker signal outside of summer, and the restrictive sample size -- for a seasonal ZW3 phase bin, the sample size is approximately 20-25. This is particularly clear in the MME mean covariance maps by season, shown in Figure (?), indicating the seasonal variability of poleward Rossby wave propagation is relatively well-representation. 

## Conclusion

Models generally perform well, however, there remains a bias toward zonal-symmetry in representation of the SAM. It seems as though models exaggerate the connection between the two fields found in ERA-5; there appears to be more internal noise disrupting or obscuring the connections than the models are able to simulate, commonly resulting in a broad, spatially coherent storm track in HF variance-SAMI covariance maps. Where there is less covariance in the Pacific Z500 field, there is similarly less covariance in the HF variance field for all models, but this direct relationship is not present in the reanalyses.