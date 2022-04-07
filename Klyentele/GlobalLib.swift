//
//  GlobalLib.swift
//  Klyentele
//
//  Created by Devin B on 4/6/22.
//

import Foundation
import SwiftUI


//Assets and Global Library

struct NormalButton: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .foregroundColor(Color(#colorLiteral(red: 0, green: 0.83, blue: 0.6, alpha: 1)))
            .frame(width: 138, height: 46)
            .font(.custom("Montserrat", size: 24))
            .background(
                RoundedRectangle(cornerRadius: 24)
                    .fill(Color(#colorLiteral(red: 0.949999988079071, green: 0.949999988079071, blue: 0.949999988079071, alpha: 1)))
                    .frame(width: 138, height: 46))
    }
}
