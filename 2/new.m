//
//  PDMTAManager.m
//  JD4iPhone
//
//  Created by 檀兵 on 16/8/2.
//  Copyright © 2016年 JD.com, Inc. All rights reserved.
//

#import "PDMTAManager.h"
#import "WareInfoMTAModel.h"
//#import "PageTrackManager.h"
//#import "RecommendJDMTA.h"
#import "WareInfoWhiteBarInfo.h"
#import "BusinessSupportPlatformAvailableModel.h"
#import "WareInfoMTAModel.h"
#import "PDRouterManager.h"
#import <THCoreComponentModule/RecommendJDMTA.h>
#import <JDBRouterModule/JDBRouterModule-umbrella.h>

@implementation PDMTAManager

+ (PDMTAManager *)sharePDMTAManager {
    static PDMTAManager *MTAManager;
    static dispatch_once_t token;
    dispatch_once(&token, ^{
        MTAManager = [[[self class] alloc] init];
    });
    return MTAManager;
}

- (void)eBookExpo:(NewProductModel *)wareModel {
    if (wareModel.eBookModel) {
        NSMutableDictionary *param = [wareModel.wareInfoMTAModel getParamByKeys:@[@"shop_id", @"sku_tag"]];
        [param setObject:@"Productdetail_MainPage" forKey:@"page_id"];
        [JDMTA_Interface jdmta_event_click:@"PDMTAManager"
                                 PageParam:wareModel.wareInfoMTAModel.wareId
                                   EventID:@"Productdetail_EbookExpo"
                                 EventName:@"eBookExpo:"
                                ParamValue:nil
                              NextPageName:nil
                                    params:param];
    }
}

- (void)addCart_OverSea:(NewProductModel *)model {
    // appsFlyer 埋点
    NSMutableDictionary *af_values = [NSMutableDictionary dictionary];
    
    // af_content_type/内容类别（加车sku的一级分类）（目前只有商详确认可传）
    [af_values setObject:@"THB" forKey:@"af_currency"];
    
    if (JDUtils.validateString(model.buyCount)) {
        [af_values setObject:model.buyCount forKey:@"af_quantity"];
    }
    if (JDUtils.validateString(model.categoryId1)) {
        [af_values setObject:model.categoryId1 forKey:@"af_content_type"];
    }
    if (JDUtils.validateString(model.name)) {
        [af_values setObject:model.name forKey:@"af_content"];
    }
    if (JDUtils.validateString(model.productCode)) {
        [af_values setObject:model.productCode forKey:@"af_content_id"];
    }
    if (JDUtils.validateString(model.priceInfo.jdPrice.value)){
        [af_values setObject:model.priceInfo.jdPrice.value forKey:@"af_price"];

    }
    
    NSMutableDictionary *af_Dict = [NSMutableDictionary dictionary];
    [af_Dict setObject:@"af_add_to_cart" forKey:@"eventName"];
    [af_Dict setObject:af_values forKey:@"values"];
    
    [JDRouter openURL:@"router://THFAFCPAiOSClientModule/logEventAppsFlyer"
                  arg:af_Dict
                error:nil
           completion:nil];
    
    // fireBase埋点
    NSMutableDictionary *fire_value = [NSMutableDictionary dictionary];
    
    NSMutableDictionary *fire_item = [NSMutableDictionary dictionary];
    NSMutableArray *mut_fire_arr = [[NSMutableArray alloc] init];
    
    [fire_item setObject:@"THB" forKey:@"Currency"];
    if (JDUtils.validateString(model.buyCount)) {
        [fire_item setObject:[NSNumber numberWithInteger:[model.buyCount integerValue]] forKey:@"QUANTITY"];
    }
    if (JDUtils.validateString(model.categoryId1)) {
        [fire_item setObject:model.categoryId1 forKey:@"ITEM_CATEGORY"];
    }
    if (JDUtils.validateString(model.name)) {
        [fire_item setObject:model.name forKey:@"ITEM_NAME"];
    }
    if (JDUtils.validateString(model.productCode)) {
        [fire_item setObject:model.productCode forKey:@"ITEM_ID"];
    }
    if (JDUtils.validateString(model.jdPrice)) {
        [fire_item setObject:[NSNumber numberWithDouble:[model.jdPrice doubleValue]] forKey:@"PRICE"];
    }
    
    
    [mut_fire_arr addObject:fire_item];
    [fire_value setObject:mut_fire_arr forKey:@"items"];
    
    NSMutableDictionary *fire_Dict = [NSMutableDictionary dictionary];
    [fire_Dict setObject:@"ADD_TO_CART" forKey:@"eventName"];
    [fire_Dict setObject:fire_value forKey:@"values"];
    
    
    [JDRouter openURL:@"router://THFAFCPAiOSClientModule/logEventFirebase"
                  arg:fire_Dict
                error:nil
           completion:nil];
    
    // faceBook埋点
    NSMutableDictionary *fb_value = [NSMutableDictionary dictionary];
    [fb_value setObject:@"THB" forKey:@"Currency"];
    if (JDUtils.validateString(model.productCode)) {
        [fb_value setObject:model.productCode forKey:@"ContentID"];
    }
    if (JDUtils.validateString(model.name)) {
        [fb_value setObject:model.name forKey:@"Content"];
    }
    NSMutableDictionary *fb_Dict = [NSMutableDictionary dictionary];
    [fb_Dict setObject:@"Added To Cart" forKey:@"eventName"];
    [fb_Dict setObject:af_values forKey:@"values"];
    
    [JDRouter openURL:@"router://THFAFCPAiOSClientModule/logEventFacebook"
                  arg:fb_Dict
                error:nil
           completion:nil];

}
@end
