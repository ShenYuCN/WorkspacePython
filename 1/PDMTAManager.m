
    [fire_item setObject:@"THB" forKey:@"Currency"];
    if (JDUtils.validateString(model.buyCount)) {
        [fire_item setObject:[NSNumber numberWithInteger:[model.buyCount integerValue]] forKey:@"QUANTITY"];
    }
    
